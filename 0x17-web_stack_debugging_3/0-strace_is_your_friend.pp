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
