#fix 500 error on apache worldpress web server using strace
exec { '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php': }
