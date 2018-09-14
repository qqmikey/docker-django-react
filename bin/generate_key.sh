#!/bin/bash

if [[ ! -f `~/.ssh/id_rsa.pub` ]]; then
ssh-keygen
ssh-agent /bin/bash
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
fi

echo 'Done.'