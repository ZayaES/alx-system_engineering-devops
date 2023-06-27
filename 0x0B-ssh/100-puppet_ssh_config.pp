-- edits the config file for client ssh --
file { '~/.ssh/config':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0600',
  content => 'Host your_server
    HostName <your_server_hostname_or_ip>
    User <your_username>
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no',
}

