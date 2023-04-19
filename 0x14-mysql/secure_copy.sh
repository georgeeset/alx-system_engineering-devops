#!/bin/bash
set -e

# user friendly copy files remotely with ssh key

read -p "Destination ip: " destination_ip
if [[ $destination_ip == "" ]]
then
    echo "empty destination ip"
    exit 1
fi

# -p option instructs to prompt user
read -p "destination user name: " destination_user
if [[ $destination_user == "" ]]
then
    echo "empty user name"
    exit 1
fi

read -p "Source file location: " source_file
if [[ -z $source_file ]]
then
    echo "empty source file"
    exit 1
fi

read -p "File destination (enter for default): " destination_file

read -p "ssh private key location: " ssh_key
if [[ $ssh_key == "" ]]
then
    echo "empty ssh key"
    exit 1
fi

scp -i $ssh_key $source_file $destination_user@$destination_ip:/home/$destination_user/$destination_file
