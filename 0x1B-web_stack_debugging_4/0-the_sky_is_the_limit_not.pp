# have high amount of request

exec {'search and replace':
  provider => shell,
  before   => Exec['restart'],
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
