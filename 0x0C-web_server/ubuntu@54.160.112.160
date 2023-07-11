#!/usr/bin/env bash
# Install NGINX package

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me http:\/\/spacedigit.tech\/home.html permanent;/" /etc/nginx/sites-available/default ; sudo service nginx restart; sudo service nginx reload',
}

