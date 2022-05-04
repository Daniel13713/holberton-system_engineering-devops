#!/usr/bin/env bash
sudo apt update
sudo apt install wget -y
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
    # Select option
    ubuntu bionic
    MySQL 8.0
    MySQL 5.7
    Ok # Choose the last otpion Ok and click OK
sudo apt-get update

sudo apt-get install -y libtinfo5
sudo apt-get install -y libmecab2

wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-common_5.7.37-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-common_5.7.37-1ubuntu18.04_amd64.deb

wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-community-client_5.7.37-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-community-client_5.7.37-1ubuntu18.04_amd64.deb

wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-client_5.7.37-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-client_5.7.37-1ubuntu18.04_amd64.deb

wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-community-server_5.7.37-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-community-server_5.7.37-1ubuntu18.04_amd64.deb

wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-server_5.7.37-1ubuntu18.04_amd64.deb
sudo dpkg -i mysql-server_5.7.37-1ubuntu18.04_amd64.deb

sudo mysql -u root -p

###############3 to solve problems ############################
#sudo apt-cache policy mysql-server
#sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
#sudo apt --fix-broken
#sudo mysql_secure_installation
#mysql -u root -p
