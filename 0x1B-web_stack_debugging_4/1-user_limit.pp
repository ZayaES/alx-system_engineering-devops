# Increased Files opened

exec {'find and replace':
  provider => shell,
  before   => Exec['replace-2'],
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
}

exec {'find and replace2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
