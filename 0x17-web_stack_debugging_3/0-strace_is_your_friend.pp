# resolve server error 500
$str = "<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>
        "
file { '/var/www/html/index.html':
      ensure  => 'file',
      content => $str,
      owner   => 'root',
      group   => 'root',
      mode    => '0611',

}
# Fixing apache error
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
