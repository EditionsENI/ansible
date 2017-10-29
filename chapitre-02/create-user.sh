#!/bin/sh

user_uid=`id -u exploit`
if [ -z "$user_uid" ]; then
  echo "Création utilisateur exploit"
  useradd exploit
else
  echo "Utilisateur exploit existant"
fi
