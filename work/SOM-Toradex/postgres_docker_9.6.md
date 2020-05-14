## `onStartup.sh`

    #!/bin/bash
    sudo docker container rm --force databasecontainer > /dev/null 2>&1
    docker run -dit --restart unless-stopped --name databasecontainer    -v /mnt/hdd/postgresql/archivedir:/mnt/hdd/postgresql/archivedir -v /mnt/hdd/postgresql/9.6/main:/var/lib/postgresql/data -p 5432:5432 postgres_image

**Volumes mounted ** : 

- `/mnt/hdd/postgresql/archivedir` mounted to `mnt/hdd/postgresql/archivedir` inside container
- `/mnt/hdd/postgresql/9.6/main` mounted to `/var/lib/postgresql/data` inside container
- `/var/lib/docker` on host 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMjQ2MjYzMTddfQ==
-->