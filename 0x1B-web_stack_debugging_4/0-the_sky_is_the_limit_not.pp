#Change the limit of open files in a query
exec { 'Change_limit':
  command  => 'sudo sed -i "s/-n 15/-n 4096/" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
