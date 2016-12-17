#!/usr/bin/env python
# -*- coding: utf-8 -*-


from modules import core
import argparse

__version__='3.0'
__description__='''\
  ___________________________________________
  
  Author: freakymonk
  Github: https://github.com/rajeshmajumdar
  ___________________________________________
'''

def getinfo(domain, resolve):
	# Resolve domain
	core.header_target(domain)
	# if [core domain.com] -> resolve is False
	# if [core -r domain.com] -> resolve is True
	core.show_resolved(domain,resolve)

	# Status code
	core.header_response_code()
	core.get_banner(domain)
	core.show_banner('code')

	# Headers
	core.header_response_head()
	core.show_banner('head')

	# Wildcard
	core.show_wildcard(domain)

def get_wordlist_targetlist(domain, path_to_worlist=False):
	# Wordlist, targetlist
	core.get_wordlist(domain, path_to_worlist)
	core.get_targetlist(domain)

def start(domain):
	# Start
	core.header_start_scan(domain)
	core.subdomain_scan()

def statistics():
	# Statistics
	core.header_stats_summary()
	core.report()

def savescan(domain):
	# Save result
	core.save_in_csv(domain)

def getzone(domain):
	core.getzone(domain)
	
def main():
	parser = argparse.ArgumentParser(
		version=__version__,
		formatter_class=argparse.RawTextHelpFormatter,
		prog='freakymonk',
		description=__description__,
		epilog = '''\
EXAMPLE:

subdomain scan with internal wordlist
  core domain.com

resolve domain name and get response headers
  core -r domain.com

check zone transfer for domain name
  core -z domain.com

The ALIAS name is marked in yellow''')

	parser.add_argument('domain', help='specific target domain, like domain.com')

	parser.add_argument('-w', help='specific path to wordlist file',
						nargs=1, dest='wordlist', required=False)

	parser.add_argument('-r', '--resolve', help='resolve ip or domain name',
						action='store_true', required=False)

	parser.add_argument('-z', '--zone', help='check for zone transfer',
						action='store_true', required=False)

	args = parser.parse_args()

	# args strings
	domain = args.domain
	wlist = args.wordlist
	if wlist: wlist = wlist[0]

	# args True or False
	resolve = args.resolve
	zone = args.zone

	# [core -r domain.com]
	if domain and resolve and not zone:
		# resolve = True
		getinfo(domain, resolve)

	# [core -z domain.com]
	elif domain and zone and not resolve:
		getzone(domain)

	# [core domain.com]
	elif domain and not resolve and not zone:
		# resolve = False
		getinfo(domain, resolve)
		
		if wlist:
			get_wordlist_targetlist(domain, wlist)
		else:
			# get_wordlist_targetlist(domain,path_to_worlist=False)
			# no wlist
			get_wordlist_targetlist(domain)
			
		start(domain)
		statistics()
		savescan(domain)

	else:
		exit('error arguments: use core -h to help')

if __name__ == '__main__':
	main()
