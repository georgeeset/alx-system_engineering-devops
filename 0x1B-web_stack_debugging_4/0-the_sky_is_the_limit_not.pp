#improve performance of nginx by increasing maximum number of requests

exec { 'increase maximum number to 10000 request ':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/bin'
  }

exec {'restart nginx with code':
  command => 'sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
  }
