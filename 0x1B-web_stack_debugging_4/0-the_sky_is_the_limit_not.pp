# increases the ulimit of nginx default to accommade high volume of requests

exec {'/etc/default/nginx':
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2048\"' /etc/default/nginx"
}
