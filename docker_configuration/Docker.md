# Docker

## Installation:

### Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

### Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


sudo docker run hello-world


-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------


## Portainer 
> Docker management via web

```sh
docker run -d \
-p 9000:9000 \
--name=portainer \
--restart=unless-stopped \
-v /var/run/docker.sock:/var/run/docker.sock \
-v ./data:/data  ngxson/portainer-ce-without-annoying:latest
```


## VAULTWARDEN
> bitwarden self hosted : then use keyguard on Android, Bitwarden on iPad

```sh
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      DOMAIN: "https://vault.oblivion.com"
    volumes:
      - ./vw-data/:/data/
    ports:
      - 10.0.0.3:1999:80

```

**On linux**:
```sh
snap install bitwarden; 
```
create file: ` ~/.local/share/applications/bitwarden_bitwarden.desktop `
```sh
[Desktop Entry]
X-SnapInstanceName=bitwarden
Name=Bitwarden
X-SnapAppName=bitwarden
Exec=/home/alby/.bitwarden-launch.sh
Terminal=false
Type=Application
Icon=/snap/bitwarden/current/meta/gui/icon.png
StartupWMClass=Bitwarden
GenericName=Password Manager
Comment=Password Manager
MimeType=x-scheme-handler/bitwarden;
Categories=Utility;
```
and create: `~/.bitwarden_launch.sh`: 
```sh
#!/bin/bash
/snap/bin/bitwarden --ignore-certificate-errors
```



## Nextcloud
> for calendar, contacts and drive, reminders and task

```yml
version: '3.7'

services:
  # Database service (MariaDB)
  db:
    image: mariadb:10.6
    container_name: nextcloud-db
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_PASSWORD: nextcloud
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
    volumes:
      - ./nextcloud_db_data:/var/lib/mysql
    networks:
      - nextcloud-network

  # Nextcloud service
  nextcloud:
    image: nextcloud:latest
    container_name: nextcloud
    restart: always
    depends_on:
      - db
    environment:
      MYSQL_PASSWORD: nextcloud
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_HOST: db
    ports:
      - "9443:80"
      - "12443:443"  # Optional for HTTPS (if you set up SSL)
    volumes:
      - ./nextcloud_data:/var/www/html
      - ./nextcloud_config:/var/www/html/config
      - ./nextcloud_apps:/var/www/html/apps
    networks:
      - nextcloud-network

networks:
  nextcloud-network:
    driver: bridge

```




###  Feishin
> jellyfin music player

```yml
services:
    feishin:
        container_name: feishin
        image: 'ghcr.io/jeffvli/feishin:1.0.1-beta.1'
        environment:
            - SERVER_NAME=Albyfin # pre defined server name
            - SERVER_LOCK=true # When true AND name/type/url are set, only username/password can be toggled
            - SERVER_TYPE=jellyfin # navidrome also works
            - SERVER_URL= 10.0.0.3:8096
            - PUID=1000
            - PGID=1000
            - UMASK=002
            - TZ=Europe/Rome
        ports:
            - 9180:9180
        restart: unless-stopped

```

## Caddy
> to make Radicale in HTTPS for iPad (since do not allow customization of http)

!! **important** add to the DNS the rewriting of the website "cloud.oblivion.com" // on router or AdGuardHome

```sh
docker run -d \
  --name caddy \
  -p 443:443 \
  --restart=unless-stopped  \
  --cap-add=NET_BIND_SERVICE \
  -v $PWD/Caddyfile:/etc/caddy/Caddyfile \
  -v $PWD/ssl/key.pem:/etc/ssl/key.pem \
  -v $PWD/ssl/cert.pem:/etc/ssl/cert.pem \
  caddy


```
 
*creating the folder mycerts inside caddy*: `sudo docker exec -it caddy sh ; mkdir /etc/ssl/mycerts`
```Caddy
cloud.oblivion.com:443 {
    tls /etc/ssl/cert.pem /etc/ssl/key.pem
    reverse_proxy http://10.0.0.3:9443
}

vault.oblivion.com:443 {
    tls /etc/ssl/cert.pem /etc/ssl/key.pem
    reverse_proxy http://10.0.0.3:1999
}

jelly.oblivion.com:443 {
    tls /etc/ssl/cert.pem /etc/ssl/key.pem
    reverse_proxy http://10.0.0.3:8096
}

## TO COPY INSIDE 
# sudo docker cp ssl/cert.pem caddy:/srv/cert.pem
# sudo docker cp ssl/cert.pem caddy:/srv/cert.pem
```



## Immich
> a collection to manage photos
> installed on PC with external library on NAS, idk all on NAS didn't work and anyway, it's better like that thus these app (phoptoprism/immich) do a lot of files

Docker_compose
```yml
name: immich

services:
  immich-server:
    container_name: immich_server
    image: ghcr.io/immich-app/immich-server:${IMMICH_VERSION:-release}
    # extends:
    #   file: hwaccel.transcoding.yml
    #   service: cpu # set to one of [nvenc, quicksync, rkmpp, vaapi, vaapi-wsl] for accelerated transcoding
    volumes:
      # Do not edit the next line. If you want to change the media storage location on your system, edit the value of UPLOAD_LOCATION in the .env file
      - ${UPLOAD_LOCATION}:/data
      - /etc/localtime:/etc/localtime:ro
      - /mnt/ARCHIVE/Visual/YEARS/:/mnt/ARCHIVE/Visual/YEARS/
    env_file:
      - .env
    ports:
      - '2283:2283'
    depends_on:
      - redis
      - database
    restart: always
    healthcheck:
      disable: false

  ### commented because who cares about it, just resource wasting for inaccurate results
  ##### immich-machine-learning:
  #####   container_name: immich_machine_learning
  #####   # For hardware acceleration, add one of -[armnn, cuda, rocm, openvino, rknn] to the image tag.
  #####   # Example tag: ${IMMICH_VERSION:-release}-cuda
  #####   image: ghcr.io/immich-app/immich-machine-learning:${IMMICH_VERSION:-release}
  #####   # extends: # uncomment this section for hardware acceleration - see https://immich.app/docs/features/ml-hardware-acceleration
  #####   #   file: hwaccel.ml.yml
  #####   #   service: cpu # set to one of [armnn, cuda, rocm, openvino, openvino-wsl, rknn] for accelerated inference - use the `-wsl` version for WSL2 where applicable
  #####   volumes:
  #####     - model-cache:/cache
  #####   env_file:
  #####     - .env
  #####   restart: always
  #####   healthcheck:
  #####     disable: false

  redis:
    container_name: immich_redis
    image: docker.io/valkey/valkey:8-bookworm@sha256:facc1d2c3462975c34e10fccb167bfa92b0e0dbd992fc282c29a61c3243afb11
    healthcheck:
      test: redis-cli ping || exit 1
    restart: always

  database:
    container_name: immich_postgres
    image: ghcr.io/immich-app/postgres:14-vectorchord0.4.3-pgvectors0.2.0@sha256:32324a2f41df5de9efe1af166b7008c3f55646f8d0e00d9550c16c9822366b4a
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_DB: ${DB_DATABASE_NAME}
      POSTGRES_INITDB_ARGS: '--data-checksums'
      # Uncomment the DB_STORAGE_TYPE: 'HDD' var if your database isn't stored on SSDs
      # DB_STORAGE_TYPE: 'HDD'
    volumes:
      # Do not edit the next line. If you want to change the database storage location on your system, edit the value of DB_DATA_LOCATION in the .env file
      - ${DB_DATA_LOCATION}:/var/lib/postgresql/data
    shm_size: 128mb
    restart: always

volumes:
  model-cache:
```


