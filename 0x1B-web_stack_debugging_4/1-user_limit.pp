# Allow holberton user to use server

exec {'allow user':
  provider => shell,
  command  => 'sudo echo "AllowUsers holberton" >> /etc/ssh/ssh_config',
  before   => Exec['allow user'],
}

#exec {'replace-2':
#  provider => shell,
#  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
#}
