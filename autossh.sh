#!/bin/bash

# autossh -f -M 0 -nNT -R 80:localhost:8080 serveo.net

createTunnel() {
    /usr/bin/autossh -f -M 0 -nNT -R 80:localhost:8080 serveo.net
    if [[ $? -eq 0 ]]; then
        echo Tunnel to created successfully
    else
        echo An error occurred creating a tunnel to $REMOTEHOST RC was $?
    fi
}

## Run the 'ls' command remotely.  If it returns non-zero, then create a new connection
result=$(ps -ef | grep autossh | grep -v grep | wc -l)
if [[ $result -eq 0 ]]; then
    echo Creating new tunnel connection
    createTunnel
fi