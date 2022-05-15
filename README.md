# Cyrecon
Cyrecon is a tool for hackers and penetration testers to perform  recon on websites and identify vulnerabilities or information that might lead to them breaking in<br/>
<br/>
It is a tool written in python that enhances your recon automation, it's fast and gives out better and well arranged results

![alt text](https://github.com/cy-cus/Cyrecon/blob/main/images/Screenshot%20from%202022-05-14%2021-59-52.png)

# INSTALLATION
Cyrecon is tested to only work in linux distros

Have python 3 installed

```
git clone https://github.com/cy-cus/Cyrecon.git
cd Cyrecon
pip install -r requirements.txt
```
# Cyrecon provides detailed information such as :



Whois information

SSL Certificate Information

Header Information

Crawler Returns

* html links
* Javascript links and files
* Internal Links
* External Links
* Images
* robots.txt
* sitemaps
* css links
* Links from Wayback Machine from Last 1 Year
* DNS Enumeration

A, AAAA, ANY, CNAME, MX, NS, SOA, TXT Records
DMARC Records
Subdomain Enumeration


Port Scan

* Scans for the top 1000 ports with Standard Services


Output Formats
* txt
* xml
* csv

# USAGE
```
usage: Cyrecon.py [-h] [--subdomains] [--crawl] [--dns] [--ports] [--whois] [--headers] [--ssl] [--trace] [--full] [--threads THREADS] [--timeout TIMEOUT] [--redirect] [-dnscustom DNSCUSTOM] [-ext EXT] [-o O]
                  url

CyRecon :) Happy Hacking!

positional arguments:
  url                   Website URL

optional arguments:
  -h, --help            show this help message and exit
  --subdomains          Subdomain Enumeration
  --crawl               Crawl and Scan The Website
  --dns                 DNS Enumeration
  --ports               Fast Port Scan
  --whois               Whois Lookup
  --headers             Header Information
  --ssl                 SSL Certificate Information
  --trace               Traceroute
  --full                Full Recon On The Website

Extra Options:
  --threads THREADS     Number of Threads [ Default : 40 ]
  --timeout TIMEOUT     Request Timeout [ Default : 30.0 ]
  --redirect            Allow Redirect [ Default : False ]
  -dnscustom DNSCUSTOM  Custom DNS Servers [ Default : 1.1.1.1 ]
  -ext EXT              File Extensions [ Example : txt, xml, php ]
  -o O                  Export Output [ Default : txt, Others : xml, csv ]
```
