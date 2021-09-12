## FavFreak - Weaponizing favicon.ico for BugBounties , OSINT and what not

![FacFreak](https://raw.githubusercontent.com/devanshbatham/FavFreak/master/static/logo.PNG)

### Detailed Description about this can be found here : 
Read Blog here : https://medium.com/@Asm0d3us/weaponizing-favicon-ico-for-bugbounties-osint-and-what-not-ace3c214e139

### Introduction 

I have created this tool for making my work easier when it comes to recon using Favicon hashes, it takes a list of urls (with https or http protocol) from stdin ,then it fetches favicon.ico and calculates its hash value. It sorts the domains/subdomains/IPs according to their favicon hashes and the most interesting part is , It matches calculated favicon hashes with the favicon hashes present in the fingerprint dictionary , If matched then it will show you the results in the output, there is option to generate shodan dorks as well (that is pretty basic and you can do it manually as well)

### How to install and use 

Note : Tested with python3.6.9 on Ubuntu/Kali

```
$ git clone https://github.com/devanshbatham/FavFreak
$ cd FavFreak
$ virtualenv -p python3 env
$ source env/bin/activate
$ python3 -m pip install mmh3
$ cat urls.txt | python3 favfreak.py 

```

Example Run : 

Note : URLs must begin with either http or https

```
$ cat urls.txt
https://example.com
https://test-example.com
http://hack-example.com
.. .. .. .. 
.. .. .. .. 
AND SO ON 
```

`$ cat urls.txt | python3 favfreak.py -o output`

**Fetching /favicon.ico and generating hashes :**

![enter image description here](https://raw.githubusercontent.com/devanshbatham/FavFreak/master/static/favfreak.PNG)


**Subdomains/IPs Sorted according to their Favicon hashes :**

![favicon hashes](https://cdn-images-1.medium.com/max/1200/1*sqv1KLo5BBaLKSGSUwFUfw.png)


**FingerPrint Based favicon Hash detection :**

![enter image description here](https://cdn-images-1.medium.com/max/1200/1*2ncy9qEy9_-6CMDYLUa9XA.png)


**Fingerprint dictionary looks like this :**
![enter image description here](https://cdn-images-1.medium.com/max/1200/1*Tnn02JMqeZmIE-XSeSSFvw.png)


### Add your own fingerprints

```
Edit favfreak.py , you will find a dictionary named 'fingerprint' , 
Add your fingerprints in that dictionary !

```

### Contact

Shoot my DM : [@0xAsm0d3us](https://twitter.com/0xAsm0d3us)

## __Want to support my work?__
If you think my work has added some value to your existing knowledge, then you can [Buy me a Coffee here](https://www.buymeacoffee.com/Asm0d3us) (and who doesn't loves a good cup of coffee?')


[![name](https://img.buymeacoffee.com/api/?url=aHR0cHM6Ly9jZG4uYnV5bWVhY29mZmVlLmNvbS91cGxvYWRzL3Byb2ZpbGVfcGljdHVyZXMvMjAyMS8wOS8wMGU4ZGJjODc0NzI0MmRjYTJmNGJkMmMzMzQ1ODUzZC5wbmdAMzAwd18wZS53ZWJw&creator=Asm0d3us&is_creating=creating%20educational%20cybersecurity%20related%20content.&design_code=1&design_color=%235F7FFF&slug=Asm0d3us)](https://www.buymeacoffee.com/Asm0d3us)
