#!/usr/bin/env bash
# Bash script that sets up web server deployment

sudo apt-get update

sudo apt-get install -y nginx

sudo service nginx start

sudo mkdir -p /data/web_static/shared

sudo mkdir -p /data/web_static/releases/test/

echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed tee -i '39 i \\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
