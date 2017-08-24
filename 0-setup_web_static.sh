#!/usr/bin/env bash
# Bash script that sets up web server deployment

sudo apt-get update

sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared

sudo mkdir -p /data/web_static/releases/test

echo -e
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed tee -i '39 i \\tlocation /hbnb_static {\n\talias /data/web_static/current;\n}' /etc/nginx/sites-available/default

sudo service nginx start
sudo service nginx reload
