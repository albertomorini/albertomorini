##Jellyfin
docker pull jellyfin/jellyfin:latest
;
mkdir -p /srv/jellyfin/{config,cache}
;
docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest

## PiHole
docker run -d \
    --name pihole \
    -p 53:53/tcp -p 53:53/udp \
    -p 80:80 \
    -e TZ="America/Chicago" \
    -v "${PIHOLE_BASE}/etc-pihole:/etc/pihole" \
    -v "${PIHOLE_BASE}/etc-dnsmasq.d:/etc/dnsmasq.d" \
    --dns=127.0.0.1 --dns=9.9.9.9 \
    --restart=unless-stopped \
    --hostname pi.hole \
    -e VIRTUAL_HOST="pi.hole" \
    -e PROXY_LOCATION="pi.hole" \
    -e FTLCONF_LOCAL_IPV4="127.0.0.1" \
    pihole/pihole:latest


## MongoDB

## docker run -d -p 27017:27017 --name myMongo -v mongo-data:/data/db mongo:latest