import requests
import urllib

# HELBURUA: NAN zenbakiaren letra kalkulatzeko nagibatzaileak egiten duena simultatuko dugu

uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = {'Host': 'ws-sendingformdata.appspot.com', 'Content-type': 'application/x-www-form-urlencoded'}
# datuak hiztegi batean adieraziko ditut
edukia = {'nan': '44344861'}
# datuak inprimaki formatua duen kate batean bihurtuko ditut
# zelan=> urllib liburutegiaren bidez
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] =  str(len(edukia_encoded))
erantzuna = requests.post(uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
edukia = erantzuna.content
print(edukia)