#!/usr/bin/env bash
# setup mysql 5.7.x


sudo apt-key add signature.key

sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

sudo apt-get update

echo "now check your abailable versions"

sudo apt-cache policy mysql-server

echo "installing mysql 5.7"

sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

echo "Done"
