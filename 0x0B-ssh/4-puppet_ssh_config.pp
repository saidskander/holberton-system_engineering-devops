# Changes SSH configguration file connecting to a server without using a password

file_line {'Turn off passwd auth':
    path   => '/etc/ssh/ssh_config',
    line   => '	PasswordAuthentication no',
    match  => 'PasswordAuthentication yes',
}

file_line {'Declare identity file':
    path   => '/etc/ssh/ssh_config',
    line   => '	IdentityFile ~/.ssh/holberton',
}
