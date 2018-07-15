#!/bin/bash
if [ ! "$(pidof autossh)" ]
then
  /usr/bin/autossh -f -M 0 -nNT -R 80:localhost:8080 serveo.net &
fi