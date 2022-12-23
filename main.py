"""
ImportDiscord (1.0.0)

Can be used to download chat from a channel..
All chat may not be saved..

 : Use a Token of a user Who is in the server..
"""

from rich import print
import requests as r
import json
import time
import math
import os


print("[blue]Token : [/blue]", end="")
token = input("")

print("[blue]Channel ID : [/blue]", end="")
channel_id = input("")

print("[blue]Lmit : [/blue]", end="")
limit = input("")

print("[blue]Dump Data ? [<name>/no] [/blue]", end="")
dump = input("")


url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}"
url_2 = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=100"
appd_url = f"https://discord.com/api/v9/channels/{channel_id}/messages?before=__before__&limit=100"
headers = {
        "authorization" : token,
        "user-agent" :"Mozilla/5.0 (Macintosh; PPC Mac OS X 10_8_3 rv:6.0) Gecko/20200429 Firefox/36.0"
        }


if int(limit) <= 100:
    res = r.get(url, headers = headers)
    print(f"STATS : {res} ")
    data_ = json.loads(res.text) 
else:
    times = math.ceil(int(limit)/100)-1
    buffer = 100
    res = r.get(url_2, headers = headers)
    print(f"STATS : {res} ")
    data_ = json.loads(res.text)        
    time.sleep(0.5)
    for e in range(0,times):
        prev = data_[-1]["id"]
        res = r.get(appd_url.replace("__before__",prev), headers = headers)
        print(f"STATS : {res} ")
        data_ += json.loads(res.text)
        time.sleep(1)

if dump != "no":
    file =  open(dump,"x")
    file.write(json.dumps(data_))
    file.close()

bigG = 0
for e in data_:
    a = len(e["author"]["username"])
    if a  > bigG:
        bigG = a
print(bigG)
data = []
for e in data_:
    if e["content"] != "":
        data.append(e)
        a_d = " "*(bigG-len(e["author"]["username"]))
        print(f"[orange_red1] AUTHOr: {e['author']['username']}[/orange_red1]{a_d} [yellow1]MSg: {e['content'] }[/yellow1]")

print(f"[green]Total msgs :  {len(data)}[/green]")
