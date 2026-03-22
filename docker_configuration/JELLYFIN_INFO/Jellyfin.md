
# JELLYFIN - current installation

```sh
sudo docker pull jellyfin/jellyfin:latest

if [ ! -d "./" ]; then
    ##if not exists i creatre the configuration folders
    sudo mkdir -p ./{config,cache,media}
fi


## inside the PC, because some plugins has problem with SQLExpress in NAS, honestly it's better , less traffic ~ every tot hours start the rsync backup anyway
docker run -d --restart=unless-stopped -v ./config:/config -v ./cache:/cache -v /mnt/MEDIA/:/media --name jellyfin -p=8096:8096 jellyfin/jellyfin:latest

```

## CSS

- Dashboard> branding: `@import url('https://cdn.jsdelivr.net/gh/loof2736/scyfin@latest/CSS/scyfin-theme.css');`


# Feishin - a very cool music player (separate docker compose)

```yml
services:
    feishin:
        container_name: feishin
        image: 'ghcr.io/jeffvli/feishin:latest'
        environment:
            - SERVER_NAME=Albyfin # pre defined server name
            # - SERVER_LOCK=true # When true AND name/type/url are set, only username/password can be toggled
            - SERVER_TYPE=jellyfin # navidrome also works
            # - SERVER_URL= 10.0.0.3:8096
            - PUID=1000
            - PGID=1000
            - UMASK=002
            - TZ=Europe/Rome
        ports:
            - 9180:9180
        restart: unless-stoppeda
```


# JELLYFIN - Without password
> FOR NEW INSTALLATION READ FOR ADMIN WITHOUT PASSWORD: ~ dismiss, use the password and store, forget it (use browser that store the cache and peace)

## ----dismissed
1. From Jellyfin 10.9 the admin user need to have password
2. since this hurts my balls a lot, just pull 10.8 and then, upgrade via docker pull jellyfin
3. I stored Jellyfin 10.8.13 since I fear that one day will be removed


```sh
docker load < <file>.tar

sudo docker pull jellyfin/jellyfin:10.8.13

if [ ! -d "/mnt/MEDIA/jellyfin/" ]; then
    ##if not exists i creatre the configuration folders
    sudo mkdir -p /mnt/MEDIA/Jellyfin/{config,cache,media}
fi

docker run -d --restart=unless-stopped -v /mnt/MEDIA/Jellyfin/config:/config -v /mnt/MEDIA/Jellyfin/cache:/cache -v /mnt/MEDIA/:/media --name byjellyfin -p=8096:8096 jellyfin/jellyfin:10.8.13
```
