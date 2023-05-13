#fix 500 error on apache worldpress web server
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
