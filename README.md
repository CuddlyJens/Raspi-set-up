# Update
```
sudo apt-get update && sudo apt-get upgrade -y
```

```
sudo reboot -h
```

```
sudo git clone https://github.com/CuddlyJens/Raspi-set-up.git
```

```
sudo python3 Raspi-set-up/setup.py
```

## After Creating the first Database
```
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```
Change the value of the bind-adress from 127.0.0.1 to 0.0.0.0 so the MariaDB server accepts connections on all host IPv4 interfaces.
```
bind-address = 0.0.0.0
```
Save and close the file then you are finished. Then, restart the MariaDB service to apply the changes:
```
sudo systemctl restart mariadb
```
You can now verify the MariaDB listening status with the following command:
```
netstat -ant | grep 3306
```
