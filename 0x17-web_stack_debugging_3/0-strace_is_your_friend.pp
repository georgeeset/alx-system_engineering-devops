#fix 500 error on apache worldpress web server
exec { "correct_spell_error":
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
