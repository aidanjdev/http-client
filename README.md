# General Project Information

The purpose of this project is to develop an extensible command-line
http-client. (Though it may never see full implementation)
This purpose is met using RFC 9112 as a guideline, and Nginx as an
industry accepted HTTP server for testing. 
(Reference documentation links are found under the references heading)

# Nginx Configuration

This program is written, and tested, on a Kali Linux distribution.
That being said, the nginx server was installed using the apt utility.
`sudo apt install nginx` (You can likely use dnf in a similar fashion on RH-based distros)
The configuration file for nginx is `/etc/nginx/nginx.conf`
Under the http directive I added the following server block directive:
`
server {
    listen  127.0.0.1:80;
    server_name localhost;
    location / {
       root /var/www/html; 
    }
}
`
This directive sets up a listener on the local machine using port 80.
(Remember that utilizing port 80 will require elevated privileges running
the nginx binary)
The html root directory is where the default nginx index.html is located.
This is the resource we will be requesting during testing.

Finally, we start the server with the command:
`sudo nginx`

You can stop the server by sending a stop signal using the command:
`sudo nginx -s stop`

# Command Examples

At the time of this writing, the only request method implemented is
GET. This method is also the default. The default port is 80 but can be
specified using the -p option.

`./http_client.py http://localhost/index.html`
If your configuration is correct, this command should elicit a response
from the Nginx server. Currently the program will parse the headers of
this response, and print them to stdout.

# References

1. https://www.rfc-editor.org/rfc/rfc9112.html - RFC 9112
2. https://nginx.org/en/docs/beginners_guide.html - nginx documentation
