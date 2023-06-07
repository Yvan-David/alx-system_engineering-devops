# resolve server error 500
file { '/var/www/html/index.html':
      ensure  => 'file',
      content => 'Holberton',
      owner   => 'root',
      group   => 'root',
      mode    => '0611',

}
