# i'm a puppet manifest to install nginx
exec { '/usr/bin/env apt-get -y update' : }

-> package { 'nginx':
  ensure => installed,
  }

-> file { '/var/www/html/index.html' :
   content => 'Holberton School!',
   }

-> file_line { 'add header' :
   ensure => present,
   path   => '/etc/nginx/nginx.conf',
   line   => "\tadd_header X-Served-By ${hostname};",
   after  => '# Basic Settings',
   }

-> service { 'nginx':
   ensure => running,
   }