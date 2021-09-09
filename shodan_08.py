#!/usr/bin/python

import time
import shodan

shodan_mykey = 'FQNAMUdkeqXqVOdXsTLYeatFSpZSktdb'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '149.56.244.87'
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
        time.sleep(1.0)
        CVE = item.replace('!', '')
        print('[+] - Vulnerability', item)

        exploits = shodan_api.exploits.search(CVE)
        
        for item in exploits['matches']:
            try:
                if item.get('cve')[0] == CVE:
                    print ('[++] - Vulnerabilidade / CVE')
                    print (item.get('description'))
                    print ()
            except:
                 print('[!] - Descricao nao disponivel')


print ("-" * 60)
print ("-" * 60)
shodan_info()
shodan_portscan()
shodan_vuln()
print ("-" * 60)



