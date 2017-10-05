# SSH Server
echo "Improving security on SSH"

echo " * Disallow X11Forwarding"
sed -i "s/X11Forwarding yes/X11Forwarding no/" /etc/ssh/sshd_config

echo " * Removing Root Login"
sed -i "s/PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config

if grep -q -e 'UseDNS' /etc/ssh/sshd_config
    then echo "UseDns already present"
    else echo "UseDNS no" >> /etc/ssh/sshd_config
fi

echo "This server is owned by Chamaeleon. Goodbye." >> /etc/motd

read -e -p "SSH Allowed users (space separated) : " ssh_users
if [[ $ssh_users ]]; then
    echo "AllowUsers $ssh_users" >> /etc/ssh/sshd_config
fi

read -e -p "Setup jail? [Y/n] : " jail
if [[ ("$jail" == "y" || "$jail" == "Y" || "$jail" == "") ]]; then
    mkdir -p /var/jail/{dev,etc,lib,usr,bin}
    mkdir -p /var/jail/usr/bin
    chown root.root /var/jail
    mknod -m 666 /var/jail/dev/null c 1 3
    cp /etc/ld.so.cache /var/jail/etc
    cp /etc/ld.so.conf /var/jail/etc
    cp /etc/nsswitch.conf /var/jail/etc
    cp /etc/hosts /var/jail/etc
    cp /bin/bash /var/jail/bin/
    if grep -q -e 'Match group sshusers' /etc/ssh/sshd_config
        then echo 'already have jail'
        else echo "Match group sshusers
          ChrootDirectory /var/jail/
          X11Forwarding no
          AllowTcpForwarding no" >> /etc/ssh/sshd_config
    fi
fi


/etc/init.d/ssh restart
