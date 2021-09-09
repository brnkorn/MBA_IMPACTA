#!/usr/bin/python

import shodan

shodan_mykey = 'FQNAMUdkeqXqVOdXsTLYeatFSpZSktdb'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '179.191.78.194'
shodan_host = shodan_api.host(shodan_target)


def shodan_info():
    print ('IP alvo: ', shodan_host['ip_str'])
    print ('Organizacao:', shodan_host.get('org','n/a') )
    print ('Sistema operacional:', shodan_host.get('os','n/a') )


def shodan_portscan():
    print ('[*] - Identificando portas abertas')
    for _line in shodan_host['data']:
        print ("[+] - Porta aberta:",_line['port'])
        print ("[+] - Banner:",_line['data'])
        print ("-" * 60)


def shodan_vuln():
    print ('[*] - Lista de possiveis vulnerabilidades:')
    for item in shodan_host['vulns']:
        CVE = item.replace('!', '')
        print('[+] - Vulnerability', item)




print ("-" * 60)
print ("-" * 60)
shodan_info()
shodan_portscan()
shodan_vuln()
print ("-" * 60)



