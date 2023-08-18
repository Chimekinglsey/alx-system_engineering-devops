# Increases the ulimit of nginx default to accommodate a high volume of requests
file { '/etc/default/nginx':
    ensure  => present,
    content => "ULIMIT=\"-n 2048\"\n",
}

exec { 'reload_nginx':
    command     => '/etc/init.d/nginx reload',
    refreshonly => true,
    require     => File['/etc/default/nginx'],
}
