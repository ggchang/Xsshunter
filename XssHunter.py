import urllib
import urllib2
import pycurl
import sys
import re
import argparse

def spechar_check(url):#special char check
    special_chars="<>#&'\""
    parameters=get_Parameter(url)
    for parameter in parameters:
        paraP=re.compile(r'\w+=')
        for para in paraP.findall(parameter):
            Mid_url=url.replace(parameter,para+special_chars)
            print Mid_url
            html=urllib.urlopen(Mid_url).read()
            check_result=html.find(para+special_chars)
            print check_result
    
def post_Parameter(post_data_path):
    post_data=open(post_data_path,'rw').read()
    Parpattern=re.compile(r'\w+=\w+')
    Parameters=Parpattern.findall(post_data)
    print Parameters
    return Parameters



def get_Parameter(url):
    Parpattern=re.compile(r'\w+=\w+')
    Parameters=Parpattern.findall(url)
    return Parameters
#    for Parameter in Parameters:
#        print Parameter

if __name__=="__main__":
    Using="XssHunter V1.1"
    parser=argparse.ArgumentParser()
    parser.add_argument('-g',type=str,dest="get_url")
    parser.add_argument('-p',type=str,dest="post_data")
    args=parser.parse_args()
    url=args.get_url
    post_data_path=args.post_data
    print url
    if url:
        get_Parameter(url)
        spechar_check(url)
    elif post_data_path:
        post_Parameter(post_data_path)
    else:
        print Using
