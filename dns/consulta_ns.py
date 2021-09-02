#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
target = "yahoo.com"

def func_mx(_target):
	question = myquery.query(_target,'MX')

	for _ns in question:
		print(_ns)

func_mx(target)
