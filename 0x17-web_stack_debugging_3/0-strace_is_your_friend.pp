#fix 500 error on apache worldpress web server
exec { "correct spell error":
  path    => ['/usr/env bin', '/usr/bin '/usr/sbin', '/bin'],
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php'
}
