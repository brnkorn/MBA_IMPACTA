#!/usr/bin/python3.8

from netmiko import Netmiko

sshconn = Netmiko("11.11.11.171", username="msfadmin", password="msfadmin", device_type="linux")

print(sshconn.find_prompt())

sshconn.disconnect()
