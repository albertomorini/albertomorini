

# OTHER
> a collection of other selfhosted software that I may use


## Home Assistant
> to monitor whole stuff
`with -P uppercase expose the HOST with IP address and not just localhost`
```sh
docker run -d -P \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=MY_TIME_ZONE \
  -v /mnt/ARCHIVE/Setups/Docker/homeassistant/config/:/config \
  -v /run/dbus:/run/dbus:ro \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
```


## Homebox
> for inventory and stocks
```sh
mkdir -p /home/alby/AppSelfHosting/Homebox
chown 65532:65532 -R  /home/alby/AppSelfHosting/Homebox
sudo docker run -d \
  --name homebox \
  --restart unless-stopped \
  --publish 7745:7745 \
  --env TZ=Europe/Rome \
  --volume /home/alby/AppSelfHosting/Homebox/:/data \
  ghcr.io/sysadminsmedia/homebox:latest
```



## Syncthing
```sh
docker run -d -p 8384:8384 -p 22000:22000/tcp -p 22000:22000/udp -p 21027:21027/udp \
  --name=syncthing \
  -v /home/alby/Music/JF_Exports/:/mine/Music \
  -v /home/alby/Documents/:/mine/Documents \
  -v /mnt/ARCHIVE/Visual/stuff/:/mine/Stuff \
  -v /mnt/ARCHIVE/Visual/phones/tmp:/mine/phonestmp \
  -v /mnt/ARCHIVE/Setups/Docker/syncthing:/var/syncthing \
  --hostname=bythings \
  syncthing/syncthing:latest
```


## Radicale
> for self-hosting calendar/reminders

*installed on PC, documents folder to be independent of NAS, then copy automatically as backup via rsync*

```sh
docker run -d --name radicale \
    -p 5232:5232 \
    --restart=unless-stopped  \
    --init \
    --read-only \
    --security-opt="no-new-privileges:true" \
    --cap-drop ALL \
    --cap-add CHOWN \
    --cap-add SETUID \
    --cap-add SETGID \
    --cap-add KILL \
    --pids-limit 50 \
    --memory 256M \
    --health-cmd="curl --fail http://localhost:5232 || exit 1" \
    --health-interval=30s \
    --health-retries=3 \
    -v ./:/data \
    tomsquest/docker-radicale
```

## WebDav
> for backup (GrapheneOS)

```sh
docker run --restart always -v /mnt/BACKUP/WEBDAV_PIXEL9/:/var/lib/dav \
    -e AUTH_TYPE=Basic -e USERNAME=alby -e PASSWORD=$PSW$ \
    --name=webdavBackupPixel9 \
    --publish 9120:80 -d bytemark/webdav
```


## Uptime Kuma
> to check the online/offline of website

```yml
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1
```

## Vikunja.io
> project management

- install the server (downloadable from the official website)
- then change in /etc/vikunja the config file setting the timezone = "Europe/Rome" 
- ip:9011 > create account and then login

```sh
mkdir $PWD/files $PWD/db
chown 1000 $PWD/files $PWD/db

sudo docker run -d -p 9011:3456 \
  --name vikunja  \
--restart=unless-stopped  \
 -v $PWD/files:/app/vikunja/files \
 -v $PWD/db:/db \
 -e VIKUNJA_CORS_ORIGINS=* \
  -e VIKUNJA_CORS_ENABLE=true \
  -e VIKUNJA_SERVICE_PUBLICURL="http://10.0.0.3:9011" \
 vikunja/vikunja:latest

```

## Homarr
> hub self hosted 

```sh
sudo docker run  \
  --name homarr \
  --restart unless-stopped \
  -p 80:7575 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ./appdata:/appdata \
  -e SECRET_ENCRYPTION_KEY='296a658793d9cc94af955281c2867d95ee87a1f958a45ef92772740182c690cf' \
  -d ghcr.io/homarr-labs/homarr:latest
  
```


## Dash. (dashdot)
> system monitor for NAS and PC

```sh
sudo docker run -d \
  -p 3001:3001 \
  --restart=unless-stopped  \
  --privileged \
  --name dashdot \
  -e  DASHDOT_ENABLE_CPU_TEMPS=true \
  -e  DASHDOT_ALWAYS_SHOW_PERCENTAGES=true \
  mauricenino/dashdot
```
*for TrueNAS (docker already installed)*
```sh
sudo docker run -d \
  -p 3001:3001 \
  -v /home/truenas_admin/docker_dash/:/mnt/host/:ro \
  --restart=unless-stopped  \
  --privileged \
  --name dashdot \
  -e  DASHDOT_ENABLE_CPU_TEMPS=true \
  -e  DASHDOT_ALWAYS_SHOW_PERCENTAGES=true \
  mauricenino/dashdot
```
fix fs:
```sh
sudo docker exec -it doshdat sh
apk --no-cache add coreutils && kill -2 1
```