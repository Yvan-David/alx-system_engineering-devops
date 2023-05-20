# define config file
$str = " Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no "
file { '~/.ssh/config' :
    ensure  => file,
    content => $str,
}