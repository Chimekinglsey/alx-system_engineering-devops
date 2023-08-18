# Fix problem of high amount files opened

exec {'find_and_replace':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 20000/" /etc/security/limits.conf',
  before   => Exec['replace'],
}

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 30000/" /etc/security/limits.conf',
}
