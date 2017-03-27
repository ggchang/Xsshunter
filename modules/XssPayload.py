#https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20injection

import string
import re
import urllib
import argparse

def check_safe(text):
    text=string.lower(text)
    alert_patt1=re.compile(r'\<.*\>.*alert\(.*\).*\<\/.*\>')
#    alert_patt1=re.compile(r'\<img|script)\>.*alert\(.*\).*\<\/(script|img)+\>')
    alert_patt2=re.compile(r'.*alert\(.*\).*>')
    javascript_patt=re.compile(r'\<.*javascript\:alert\(.*\).*\>')
        
    result=alert_patt1.findall(text)
    print result
    return result

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-p',type=str,dest="text")
    args=parser.parse_args()
    text=args.text
    a=check_safe(text)
