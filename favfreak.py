#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool
from time import time as timer
from urllib.request import urlopen
import mmh3
import codecs
import sys
import ssl
import argparse
import os
import errno
from os import path



def main():
    urls = []
    a = {}
    for line in sys.stdin:
        if line.strip()[-1] == "/":
            urls.append(line.strip() + "favicon.ico")
        else:
            urls.append(line.strip() + "/favicon.ico")
    
    def fetch_url(url):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urlopen(url, timeout=5,context=ctx)
            favicon = codecs.encode(response.read(),"base64")
            hash = mmh3.hash(favicon)
            key = hash
            a.setdefault(key, [])
            a[key].append(url)

            return url, hash, None
        except Exception as e:
            return url, None, e

    start = timer()
    results = ThreadPool(20).imap_unordered(fetch_url, urls)
    for url, hash, error in results:
        if error is None:
            print("\u001b[32m[INFO]\u001b[0mFetched %r" % ( url[:-12]))
        else:
            print("\u001b[31m[ERR]\u001b[0m Not Fetched %r " % (url[:-12]))
    print("\n")
    print("-------------------------------------------------------------------")
    print("\u001b[32m[Favicon Hash Results] - \u001b[0m\n")
    for i,j in a.items():
        if len(j)>1:
            print("\u001b[33m[Hash]\u001b[0m " + "\u001b[32;1m" + str(i)+"\u001b[0m")
            for k in j:
                print("     " + k[:-12])
        else:
            print("\u001b[33m[Hash]\u001b[0m " + "\u001b[32;1m" + str(i)+"\u001b[0m")
            for k in j:
                print("     " + k[:-12])
        
        

    return a,urls

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='FavFreak - a Favicon Hash based asset mapper')
        parser.add_argument('-o','--output' , help = 'Output file name')
        parser.add_argument('--shodan' , help = 'Prints Shodan Dorks', action='store_true')
        args = parser.parse_args()
        if os.name == 'nt':
            os.system('cls')
        banner = """\u001b[32m

    \u001b[31m_______ _______ \u001b[0m\u001b[32m_    _ _______  ______ _______ _______ _     _
    |______ |_____|  \  /  |______ |_____/ |______ |_____| |____/ 
    |       |     |   \/   |       |    \u001b[31m\_ |______\u001b[0m\u001b[32m |     | |    \_

                                \u001b[35m- Coded with \u001b[31m<3\u001b[0m\u001b[35m by Devansh Batham               
                                                        
           \u001b[0m 
        """
        print(banner)
        a,urls= main()

        # add your fingerprints here :
        
        fingerprint = {

            99395752: 'slack-instance',
            878647854: 'atlasian',
            116323821: 'spring-boot',
            878647854: 'big-IP',

            }



        print("\n")
        print("-------------------------------------------------------------------")
        print("\u001b[32m[FingerPrint Based Detection Results] - \u001b[0m\n")
        for i in a.keys():
            if i in fingerprint.keys():
                print("\u001b[31m["+fingerprint[i]+"] \u001b[0m" + str(i) + " - count : " + str(len(a[i])))

        print("\n")
        if args.shodan:
            print("-------------------------------------------------------------------")
            print("\u001b[32m[Shodan Dorks] - \u001b[0m\n")
            for i in a.keys():
                if i != 0:
                    print("\u001b[34m[DORK]\u001b[0m org:\"Target-Name\" http.favicon.hash:"+str(i))

        if args.output:
            for i in a.keys():
                filename = args.output + "/" + str(i) + ".txt"
                if path.exists(filename):
                    os.remove(filename)
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc:
                        if exc.errno != errno.EEXIST:
                            raise
            
                with open(filename, "a") as f:
                    f.write('\n'.join(a[i]))
                    f.write("\n")
        print("-------------------------------------------------------------------")
        print("\u001b[32m[Summary]\u001b[0m\n")
        print(" \u001b[36mcount      \u001b[35mHash\u001b[0m         ")
        for i in a.keys():
            print(f"~ \u001b[36m[{len(a[i])}]  : \u001b[35m[{i}]\u001b[0m ")
        if args.output:
            print(f"\n\u001b[32m[+] Output saved here : {args.output}\u001b[0m")
    except KeyboardInterrupt:
        print("\n\u001b[31m[EXIT]KeyBoard Interrucpt Encountered \u001b[0m")