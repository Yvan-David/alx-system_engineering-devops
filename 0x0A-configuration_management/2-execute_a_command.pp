# use exec resource to kill a process
exec { 'pkill killmenow':
        command => '/bin/pkill killmenow',
}