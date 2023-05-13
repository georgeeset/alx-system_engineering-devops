# fix 500 error on wordpress files

exec { '500 error fix':
     path    => '/usr/local/bin/:/bin/'
     command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    }