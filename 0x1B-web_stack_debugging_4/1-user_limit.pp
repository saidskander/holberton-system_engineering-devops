# puppet for a user limit

exec { '/usr/bin/env sed -i "s/holberton/" /etc/security/limits.conf': }
