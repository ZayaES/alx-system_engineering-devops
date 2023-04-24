#puppet program to kill a process

exec {'killmenow':
  command    => '/usr/bin/pkill killmenow',
}
