import os

os.system('sudo apt-get update && sudo apt-get upgrade -y')

# Install GitHub
os.system('sudo apt-get install git-all -y')
# Install Docker
os.system('sudo apt install docker.io -y')
os.system('sudo curl -SL https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose')
os.system('sudo chmod +x /usr/local/bin/docker-compose')
os.system('sudo docker volume create portainer_data')
os.system('sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest')

# Install Node, NPM, Python3
os.system('sudo apt install -y \
          nodejs \
          npm \
          python3')

# Install MySQL
os.system('sudo apt install mariadb-server -y')
os.system('sudo mysql_secure_installation')

with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'w') as file:
    data = file.readlines()

print(data)
data[26] = "bind-address            = 0.0.0.0\n"

with open('/etc/mysql/mariadb.conf.d/50-server.cnf', 'w') as file:
    file.writelines(data)

os.system('sudo systemctl restart mariadb')
os.system('netstat -ant | grep 3306')
print('Setup Finished')
print('Reboot System')
os.system('sudo reboot -h')