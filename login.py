#!/usr/bin/env python3
import os
import cgi
from templates import login_page, secret_page
import secret

body = ""
header = ""

def check_cookies():
    cookies = os.environ["HTTP_COOKIE"] if os.environ["HTTP_COOKIE"] is not None else ""
    cookies = cookies.split(";")
    for cookie in cookies:
        if "logged=true" in cookie:
            return True
    return False

form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")

header += "Content-Type: text/html\r\n"

if check_cookies():
    body += secret_page(secret.username, secret.password)
elif (username == secret.username and password == secret.password):
    header += "Set-Cookie: logged=true; Max-age=60\r\n"
    header += "Set-Cookie: cookie=now\r\n"


print(header)
print(body)
