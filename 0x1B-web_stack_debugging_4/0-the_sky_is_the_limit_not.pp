#improve performance of nginx
exec { 'increase max number of open files':
  command => 'sed -i "s/15/20000/" /etc/default/nginx',
  path    => '/bin'
  }

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
  }
