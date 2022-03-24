import requests
import urllib

#datubidalketa_form_POST-en helburu berbera baina GET metodoarekin
base_uria = "http://ws-sendingformdata.appspot.com/processForm"
goiburuak = {'Host': 'ws-sendingformdata.appspot.com'}
# datuak hiztegi batean adieraziko ditut
edukia = {'nan': '44344861'}
edukia_encoded = urllib.parse.urlencode(edukia)
uria = base_uria + '?' + edukia_encoded
erantzuna = requests.get(uria, headers=goiburuak, allow_redirects=False)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
edukia = erantzuna.content
print(edukia)