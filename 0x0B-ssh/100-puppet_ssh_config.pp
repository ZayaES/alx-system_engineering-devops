# configures ssh to connect via private key

file { 'config':
  path    => '/etc/ssh/ssh_config',
  ensure  => 'present',
  mode    => '0744',
  content => 'SendEnv LANG LC_*\nHashKnownHosts yes\nHostName 100.25.149.245\nUser ubuntu\nIdentityFile ~/.ssh/school\nPreferredAuthentications publickey\nPasswordAuthentication no'
}
