# Changes SSH configguration file connecting to a server without using a password

exec { 'echo':
  path    => '/etc/ssh/sshd_config',
  command => 'echo "  IdentityFile ~/.ssh/holberton\n  PasswordAuthentication no" >> /etc/ssh/sshd_config',
  returns => [0,1],
}
