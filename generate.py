import urllib.request, json 

f = open("./dictionary.txt", "w")

words = []
with urllib.request.urlopen("https://sozluk.gov.tr/autocomplete.json") as url:
    data = json.loads(url.read().decode())

    for word in data:
        if len(word['madde']) == 5 and ' ' not in word['madde'] and '!' not in word['madde']:
            words.append(word['madde'].replace('î', 'i').replace('â', 'a').replace('û', 'u').replace('i', 'İ').replace('ı','I').upper())
for word in words:
    f.write(word+"\n")
f.close()