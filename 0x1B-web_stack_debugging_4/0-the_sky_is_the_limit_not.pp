#improve performance of nginx
exec { 'increase max number to 10000 ewquest':
  command => 'sed -i "s/100/10000/" /etc/default/nginx',
  path    => '/bin'
  }

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
  }
