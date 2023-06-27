#!/usr/bin/env bash
# Install NGINX package
package { 'nginx':
  ensure => 'installed',
}

# Configure NGINX server
file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  mode   => '0644',
  content => '
    server {
      listen 80;
      server_name _;

      location / {
        return 200 "Hello World!";
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=MjoP9GWgxe0&t=1592s
      }
    }
  ',
  require => Package['nginx'],
}

# Enable default NGINX site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart NGINX service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  hasstatus => true,
  require   => File['/etc/nginx/sites-enabled/default'],
}

