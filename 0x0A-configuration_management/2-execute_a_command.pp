# Kill a running process killmenow from the process table
exec { 'killmenow':
  command  => 'pkill killmenow',
  path     => '/usr/bin:/bin',
  onlyif   => 'pgrep killmenow',
  provider => shell,
}
