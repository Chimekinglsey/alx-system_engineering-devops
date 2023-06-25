# using Puppet to disable password login
file_line { 'disable password login':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  line => 'IdentityFile ~/.ssh/school',
}
