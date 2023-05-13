#fix 500 error on apache worldpress web server
exec {'sudo sed -i s/phpp/php/g /var/www/html/wp-settings.php'}