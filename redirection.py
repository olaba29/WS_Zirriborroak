import requests

# HELBURUA: web bezero hau eGelako orrialde naguzira konektatuko da

# HTTP eskaerak 4 eremu ditu:
# Eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
metodoa = "GET"
uria = "http://egela.ehu.eus/"
goiburuak = { 'Host': 'egela.ehu.eus' }
edukia = ""


# eskaera bidali (eskaeraren metodoa liburutegiaren metodoan adierazi)
#eta erantzuna jaso
erantzuna = requests.get(uria, headers=goiburuak, data=edukia, allow_redirects=False)

# HTTP erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(" ---- Kodea eta Deskribapena ----")
print(str(kodea) + " " + deskribapena)
location = erantzuna.headers['Location']
print("Location :" + location)

#### Eskaera berria "Location" goiburuak adierazten duen URI-ra
# HTTP eskaerak 4 eremu ditu:
# Eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
metodoa = "GET"
uria = location
goiburuak = { 'Host': 'egela.ehu.eus' }
edukia = ""

# eskaera bidali (eskaeraren metodoa liburutegiaren metodoan adierazi)
#eta erantzuna jaso
erantzuna = requests.get(uria, headers=goiburuak, data=edukia, allow_redirects=False)

# HTTP erantzunak 4 atal ditu: kodea, deskribapena, goiburuak eta edukia
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(" ---- Kodea eta Deskribapena ----")
print(str(kodea) + " " + deskribapena)
location = erantzuna.headers['Location']
print("Location :" + location)