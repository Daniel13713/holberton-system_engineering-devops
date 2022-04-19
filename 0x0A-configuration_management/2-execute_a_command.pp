#Execute a command with condiction only if a process is running
exec { 'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
