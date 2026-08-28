#!/usr/bin/env python3

import subprocess

svc = "sshd"

check_cmd = ["ps", "-C", svc]

serveice_check = subprocess.call(check_cmd)

if serveice_check == 0:
    print("the service is running")
else:
    print("the service is not running")
    print("starting it...")
    subprocess.call("systemctl", "start", "sshd")
    subprocess.call(check_cmd)