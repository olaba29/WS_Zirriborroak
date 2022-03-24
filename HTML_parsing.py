#-*- coding: UTF-8 -*-
import urllib.parse

import requests
from bs4 import BeautifulSoup
import sys

# "bilatu" zebritzuko inprimakiaren HTML kodean "<form" bilatu
# "method" atributuan datuak bidaltzeko erabili behar den metodoa adierazten da
metodo = 'POST'
# "action" atributuan datuka jasoko dituen zerbitzariaren URI-a adierazten da
uria = 'https://www.ehu.eus/bilatu/buscar/bilatu.php?lang=es'
goiburuak =  {'Host': 'www.ehu.eus', 'Content-type': 'application/x-www-form-urlencoded'}
# bidaliko den balioaren parametroaren izena
# dagokion "<input" elementuaren "name" atributua adierazten da
edukia = {'abi_ize': sys.argv[1]}
# datuak inprimaki formatuan kodifikatu
edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))
# orain "buscar" botoia sakatzen dugula emulatuko dugu
# hots, HTTP eskaera bidaltzen da
erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(" ---- Kodea eta Deskribapena ----")
print(str(kodea) + " " + deskribapena)

html = erantzuna.content

# bilaketaren emaitzak dituen HTML dokumentua parseatu
soup = BeautifulSoup(html, 'html.parser')
errenkadak = soup.find_all('td', {'class': 'fondo_listado'})
for idx, errenkada in enumerate(errenkadak):
    izen_abizena = errenkada.a.text #etiketa bera
    esteka = "hhtps://www.ehu.eus" + errenkada.a['href'] # etiketaren atributua
    print(str(idx) + "-" + izen_abizena + "-" + esteka)

