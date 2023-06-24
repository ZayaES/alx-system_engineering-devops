# creating a file with puppet 

file { '/tmp':
  path    =>     '/tmp/school',
  mode    =>     '0744',
  owner   =>     'www-data',
  group   =>     'www-data',
  content =>     'I love Puppet'
}
