# Update
```
sudo apt-get update
```

```
sudo apt-get upgrade -y
```

```
sudo reboot -h
```
# Install Docker
```
sudo apt install docker.io -y
```

```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```

```
sudo docker volume create portainer_data
```

```
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```
Docker portainer https://192.168.178.27:9443

# Install Node, NPM and Python3
```
sudo apt install nodejs -y
```
```
sudo apt install npm -y
```
```
sudo apt install python3 -y
```
# Install and setup MySQL
```
sudo apt install mariadb-server -y
```
```
sudo mysql_secure_installation
```
