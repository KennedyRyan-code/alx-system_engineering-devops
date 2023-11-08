# Puppet manifest to fix Apache 500 error issue

exec { 'fix-apache-issue':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  refreshonly => true,
  path        => '/usr/local/bin/:/bin/'
}
