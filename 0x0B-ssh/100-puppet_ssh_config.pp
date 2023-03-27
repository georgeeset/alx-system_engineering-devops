# using Puppet to make changes to our configuration file

file { '/home/vagrant/.ssh/config':
  ensure  => present,
  content => "Host 139552-web-01\n  Hostname 18.208.119.87\n User ubuntu
  	     IdentityFile ~/.ssh/school\n  BatchMode yes"
}