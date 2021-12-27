import requests
import time
import base64
import urllib.parse
from bs4 import BeautifulSoup
import re
import math

headers = {"X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1"}


def bypassLinkvertise(url):
    url = url.replace("?o=sharing", "")
    url_split = url.split("/")
    url = url_split[3] + "/" + url_split[4]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0", 
        "Accept": "application/json", 
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3", 
        "Accept-Encoding": "gzip, deflate, br", 
        "referer": "https://linkvertise.com/", 
        "Content-Type": "application/json", 
        "origin": "https://linkvertise.com/", 
        "sec-fetch-dest": "empty", 
        "sec-fetch-mode": "cors", 
        "sec-fetch-site": "same-site", 
        "cache-control": "max-age=0", 
        "te": "trailers"
    }
    r1 = requests.get(f"https://publisher.linkvertise.com/api/v1/redirect/link/static/{url}", headers=headers)
    timestamp = int(time.time() * 1000)
    o = """{"timestamp":""" + str(timestamp) + ""","random":"6548307","link_id":""" + str(r1.json()["data"]["link"]["id"]) + "}"
    o = str.encode(o)
    o = base64.b64encode(o)
    o = o.decode('utf-8')
    r2 = requests.post(f"https://publisher.linkvertise.com/api/v1/redirect/link/{url}/target", headers=headers, json={"serial": o})
    url_final = r2.json()["data"]["target"]
    url_final = urllib.parse.unquote(url_final)
    return str(url_final)

def bypassRekonise(url):
    url = url[21:]
    r = requests.get(f"https://api.rekonise.com/unlocks/{url}", headers=headers)
    try:
        return str(r.json()["url"])
    except:
        return "Une erreur est survenue."

def bypassSub2Unlock(url):
    check = requests.get(url, headers=headers)
    if check.url == url:
        pass
    else:
        return "URL invalide."
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    div_link = soup.find("div", id="theGetLink")
    url_final = urllib.parse.unquote(div_link.contents[0])
    return str(url_final)

def bypassClictune(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    script_link = soup.find("noscript")
    script_link = str(script_link)
    soup2 = BeautifulSoup(script_link, "html.parser")
    for a in soup2.find_all("a", href=True):
        link = a["href"]
    if "mylink1.biz" in link:
        url_final = link[43:-83]
        url_final = urllib.parse.unquote(url_final)
        return url_final
    else:
        return "Une erreur est survenue."

def bypassAdfLy(url):
    def isNaN(num):
        try:
            int(num)
            return False
        except:
            return True
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    mdr = soup.find_all("script")
    soup2 = BeautifulSoup(str(mdr[7]), "html.parser")
    pattern = re.compile("var ysmm = (.*);")
    lol = pattern.findall(str(soup2))
    ysmm = lol[0]
    ysmm = ysmm[1:-1]
    r = ysmm
    m = 0
    a = []
    I = ""
    X = ""
    while m < len(r):
        if m % 2 == 0:
            I += r[m]
        else:
            X = r[m] + X
        m += 1
    r = I + X
    for letter in r:
        a.append(letter)
    m = 0
    while m < len(a):
        if not isNaN(a[m]):
            R = m + 1
            while R < len(a):
                if not isNaN(a[R]):
                    S = int(a[m]) ^ int(a[R])
                    if S < 10:
                        a[m] = S
                    m = R
                    R = len(a)
                R += 1
        m += 1
    a_2 = []
    for i in a:
        a_2.append(str(i))
    r = "".join(a_2)
    r = base64.b64decode(r).decode('utf-8')
    r = r[len(r)-(len(r)-16):]
    r = r[0:len(r)-16]
    parsed = urllib.parse.urlparse(r)
    link = parsed.query[67:]
    link_final = urllib.parse.unquote(link)
    if link_final[0] != "h":
        url_temp = "h"
        url_temp += link_final
        link_final = url_temp
    return str(link_final)

def bypassShortUrlLink(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    mdr = soup.find_all("script")
    soup2 = BeautifulSoup(str(mdr[8]), "html.parser")
    pattern = re.compile("url = (.*);")
    lol = pattern.findall(str(soup2))
    url = lol[0]
    url = url[1:-1]
    url_final = urllib.parse.unquote(url)
    return str(url_final)
