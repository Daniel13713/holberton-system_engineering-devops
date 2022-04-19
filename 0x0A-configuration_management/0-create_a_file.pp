# Create a file with permission, group, owner and content
file {'school':
  ensure  => present,
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
