import urllib.request, json
for ip in range(10,31):
    with urllib.request.urlopen("http://192.168.1."+str(ip)+":8167/?format=json") as url:
        data = json.loads(url.read().decode())
        print ("192.168.1.",str(ip),": ",data["temperatures"])
