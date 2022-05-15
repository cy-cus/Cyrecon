#!/usr/bin/env python3

import os
import sys
import atexit
import socket
import requests
import datetime
import ipaddress
import tldextract
from json import loads
import argparse
import shutil
from recon_scripts.sslinfo import cert
from recon_scripts.crawler import crawler
from recon_scripts.headers import headers
from recon_scripts.dns import dnsrec
from recon_scripts.traceroute import troute
from recon_scripts.whois import whois_lookup
from recon_scripts.portscan import ps
from recon_scripts.subdom import subdomains
from recon_scripts.export import export


version = '1.0'
gh_version = ''
twitter_url = ''
discord_url = ''



home = os.getenv('HOME')
usr_data = 'recon_results/'
conf_path = '.config/cyrecon'
path_to_script = os.path.dirname(os.path.realpath(__file__))
src_conf_path = path_to_script + '/conf/'
fail = False
meta_file_path = path_to_script + '/metadata.json'
with open(meta_file_path, 'r') as metadata:
		json_data = loads(metadata.read())
		twitter_url = json_data['twitter']


R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white

art = r'''
 ██████╗██╗   ██╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║      ╚████╔╝ ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
╚██████╗   ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
 Let's hack the planet!
'''
print(f'{G}{art}{W}\n')
print(f'{G} Coded By   :{W} Cycus Pectus')
print(f'{G} Twitter   :{W} {twitter_url}')
print(' \n')





if os.path.exists(conf_path):
	pass
else:
	shutil.copytree(src_conf_path, conf_path, dirs_exist_ok=True)



parser = argparse.ArgumentParser(description=f'CyRecon :) Happy Hacking!')
parser.add_argument('url', help='Website URL')
parser.add_argument('--subdomains', help='Subdomain Enumeration', action='store_true')
parser.add_argument('--crawl', help='Crawl and Scan The Website', action='store_true')
parser.add_argument('--dns', help='DNS Enumeration', action='store_true')
parser.add_argument('--ports', help='Fast Port Scan', action='store_true')
parser.add_argument('--whois', help='Whois Lookup', action='store_true')
parser.add_argument('--headers', help='Header Information', action='store_true')
parser.add_argument('--ssl', help='SSL Certificate Information', action='store_true')
parser.add_argument('--trace', help='Traceroute', action='store_true')
parser.add_argument('--full', help='Full Recon On The Website', action='store_true')

ext_help = parser.add_argument_group('Extra Options')
ext_help.add_argument('--threads', type=int, help='Number of Threads [ Default : 40 ]')
ext_help.add_argument('--timeout', type=float, help='Request Timeout [ Default : 30.0 ]')
ext_help.add_argument('--redirect', action='store_true', help='Allow Redirect [ Default : False ]')
ext_help.add_argument('-dnscustom', help='Custom DNS Servers [ Default : 1.1.1.1 ]')
ext_help.add_argument('-ext', help='File Extensions [ Example : txt, xml, php ]')
ext_help.add_argument('-o', help='Export Output [ Default : txt, Others : xml, csv ]')
ext_help.set_defaults(
	t=40,
	T=30.0,
	r=False,
	s=True,
	sp=443,
	d='1.1.1.1',
	e='',
	m='UDP',
	p=33434,
	tt=1.0,
	o='txt')

try:
	args = parser.parse_args()
except SystemExit:
	sys.exit()

target = args.url
headinfo = args.headers
sslinfo = args.ssl
whois = args.whois
crawl = args.crawl
dns = args.dns
trace = args.trace
pscan = args.ports
full = args.full
threads = args.threads
tout = args.timeout
redir = args.redirect
sslv = args.s
sslp = args.sp
dserv = args.dnscustom
filext = args.ext
subd = args.subdomains
mode = args.m
port = args.p
tr_tout = args.tt
output = args.o


type_ip = False
data = {}
meta = {}


def banner():
	pass
	
	



def full_recon():
	headers(target, output, data)
	cert(hostname, sslp, output, data)
	whois_lookup(ip, output, data)
	dnsrec(domain, output, data)
	if type_ip is False:
		subdomains(domain, tout, output, data, conf_path)
	else:
		pass
	troute(ip, mode, port, tr_tout, output, data)
	ps(ip, output, data)
	crawler(target, output, data)


try:
	banner()

	if target.startswith(('http', 'https')) is False:
		print(f'{R}[-] {C}Protocol Missing, Include {W}http:// {C}or{W} https:// \n')
		sys.exit(1)
	else:
		pass

	if target.endswith('/') is True:
		target = target[:-1]
	else:
		pass

	print(f'{G}[+] {C}Target : {W}{target}')
	ext = tldextract.extract(target)
	domain = ext.registered_domain
	hostname = '.'.join(part for part in ext if part)

	try:
		ipaddress.ip_address(hostname)
		type_ip = True
		ip = hostname
	except Exception:
		try:
			ip = socket.gethostbyname(hostname)
			print(f'\n{G}[+] {C}IP Address : {W}{str(ip)}')
		except Exception as e:
			print(f'\n{R}[-] {C}Unable to Get IP : {W}{str(e)}')
			sys.exit(1)

	start_time = datetime.datetime.now()

	meta.update({'Version': str(version)})
	meta.update({'Date': str(datetime.date.today())})
	meta.update({'Target': str(target)})
	meta.update({'IP Address': str(ip)})
	meta.update({'Start Time': str(start_time.strftime('%I:%M:%S %p'))})
	data['module-CyRecon'] = meta

	if output != 'None':
		fpath = usr_data
		fname = fpath + hostname + '.' + output
		if not os.path.exists(fpath):
			os.makedirs(fpath)
		output = {
			'format': output,
			'file': fname,
			'export': False
		}

	if full is True:
		full_recon()

	if headinfo is True:
		headers(target, output, data)

	if sslinfo is True:
		cert(hostname, sslp, output, data)

	if whois is True:
		whois_lookup(ip, output, data)

	if crawl is True:
		crawler(target, output, data)

	if dns is True:
		dnsrec(domain, output, data)

	if subd is True and type_ip is False:
		subdomains(domain, tout, output, data, conf_path)
	elif subd is True and type_ip is True:
		print(f'{R}[-] {C}Subdomain Enumeration is Not Supported for IP Addresses{W}\n')
		sys.exit(1)
	else:
		pass

	if trace is True:
		if mode == 'TCP' and port == 33434:
			port = 80
			troute(ip, mode, port, tr_tout, output, data)
		else:
			troute(ip, mode, port, tr_tout, output, data)

	if pscan is True:
		ps(ip, output, data)


	if any([full, headinfo, sslinfo, whois, crawl, dns, subd, trace, pscan]) is not True:
		print(f'\n{R}[-] Error : {C}At least One Argument is Required with URL{W}')
		output = 'None'
		sys.exit(1)

	end_time = datetime.datetime.now() - start_time
	print(f'\n{G}[+] {C}Completed in {W}{str(end_time)}\n')

	@atexit.register
	def call_export():
		meta.update({'End Time': str(datetime.datetime.now().strftime('%I:%M:%S %p'))})
		meta.update({'Completion Time': str(end_time)})
		if output != 'None':
			output['export'] = True
			export(output, data)

	sys.exit()
except KeyboardInterrupt:
	print(f'{R}[-] {C}Keyboard Interrupt.{W}\n')
	sys.exit(130)
