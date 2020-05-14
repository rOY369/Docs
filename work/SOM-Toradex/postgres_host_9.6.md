
## Installing postgresql 

- Download source from https://ftp.postgresql.org/pub/source/v9.6.17/postgresql-9.6.17.tar.gz
- Installation
	- `./configure`
	- `make`
	- `sudo su`
	- `make install`
	- `adduser postgres`
	- `mkdir /mnt/hdd/postgresql/data`
	- `chown postgres /mnt/hdd/postgresql/data`

Systemd service file - `/etc/systemd/system/postgresql.service`

```
[Unit]
Description=PostgreSQL database server
Documentation=man:postgres(1)

[Service]
User=postgres
ExecStart=/usr/local/pgsql/bin/postgres -D /mnt/hdd/postgresql/data
ExecReload=/bin/kill -HUP $MAINPID
KillMode=mixed
KillSignal=SIGINT
TimeoutSec=0

[Install]
WantedBy=multi-user.target
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzI3MjIzMjk5XX0=
-->