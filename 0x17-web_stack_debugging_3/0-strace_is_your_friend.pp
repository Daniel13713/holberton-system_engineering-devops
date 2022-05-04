#Debugging with curl, strace and fix with puppet
exec { 'fix bug':
    command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    path    => '/bin/',
}
