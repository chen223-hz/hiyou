#!/bin/bash

rsync -rlptDv --exclude=".git" --exclude=".gitignore" --exclude="env" \
  --exclude=".DS_Store" --exclude="._.DS_Store" --exclude="*.log" \
  --exclude="*.pyc" --exclude="*.dat" --exclude="*.db" --exclude="update.sh" \
  ./* root@120.26.57.92:/home/www/hiyou/
ssh root@120.26.57.92 chown -R www-data:www-data /home/www/hiyou
#ssh root@120.26.57.92 supervisorctl restart hotspot:*
#ssh root@120.26.57.92 supervisorctl restart radiusd
