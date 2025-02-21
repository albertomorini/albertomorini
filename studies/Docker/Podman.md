An alternative to Docker Desktop, more light weight

After installing.

```sh
$ podman machine init --disk-size 10  --rootful=true -v /Volumes/MEDIA:/Volumes/MEDIA:Z -v /Volumes/ARCHIVE:/Volumes/ARCHIVE:Z albypod
```


Jellyfin example
```sh
podman run -d --restart=unless-stopped -v /Volumes/MEDIA/Jellyfin/config:/config:z -v /Volumes/MEDIA/Jellyfin/cache:/cache:z -v /Volumes/MEDIA/:/media:z --name byjellyfin -p=8096:8096 jellyfin/jellyfin:latest
```