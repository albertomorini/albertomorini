# Firewalls

Firewalls block all the traffic except the ones we allow. It operate at level 4 (ISO/OSI) and some also at level 7 (Application).

## Layer 4
Feature like:
- NAT (change the private IP with the public one) 
- Routing (send the package through networks/internet)
- Blocking/Allowing traffic
- Track active connection (see if a communication is still used or terminated)
- Support VPN connection (allow you to access to Virtual Private Network, so send some kind of package/data to it)

## NGFW / Layer 7
NextGeneration Firewalls, allows the same features of Layer 4 and more ones:
- location via geo-services, so can block/allow traffic based on the location of the user
- user 
- application and relative ports
- session (a specific identifier created from browser to allow you a better surfing)
- IP address

## Zero-trust architecture

Forcing all systems on the netowrk to explicit be allowed to communicate to different services.
*Eg
IT-Administrators should be able to use management protocols to the different services.
HR employees should be allowed to access HTTPS to the HR platforms.
Helpdesk employees can only access helpdesk related services.
Unrecognizable users can be identified and provisioned accordingly.*


## Content filtering
PiHole is an example of it, a firewall which can protect content access via HTTP by looking into a database containing allowed/blocked urls.
There are a lot of rules and datasets whose can allows or block websites by their kind, like blocking gambling/nudity/socials etc.

A firewall can identify also the application on layer 7 (ISO/OSI), next, can determinate the content being downloaded, like software/multimedia/document etc. Then, it can try to find a potential malware.

Firewall can works with different protocol:
- SMB/FTP
- HTTP
- IMAP/POP3/SMTP
- ...

## Sandboxing

A sandbox allows the system to run the executable downloaded/recieved into a protected and isolated platform, in this way firewall can verify the behaviour of the software/document.

## HTTPS
Firewall can implement cryptography, allowing or blocking the website which has the encryption key or vicerversa, hasn't.

