import orodja 
import re
import requests
import json

STEVILO_STRANI = 30
STEVILO_KNJIG_NA_STRAN = 100 

stevec = 0
slovarji_knjig = []

vzorec_knjiga = re.compile(r'<td width="100%".*?>(.*?)emsp;', re.DOTALL)

vzorec_naslov = re.compile(r'''<a class="bookTitle".*?>\n\s+<span.*?>(?P<naslov>.*?)</span>''', re.DOTALL)
vzorec_avtor = re.compile(r'<a class="authorName".*?><.*?>(?P<avtor>.*?)</span>', re.DOTALL)
vzorec_ocena = re.compile( r'></span></span>\s+(?P<ocena>.*?)\s+avg\srating', re.DOTALL)
vzorec_stevilo_volilcev = re.compile(r'<a id=".+?" href="#" .*?>(?P<stevilo_volilcev>.*?) people voted', re.DOTALL)

skupina_naslov = 'naslov'
skupina_avtor = 'avtor'
skupina_ocena = 'ocena'
skupina_stevilo_volilcev = 'stevilo_volilcev'

def html_v_knjige(vsebina):
    """Funkcija poišče posamezne knjige, ki se nahajajo v spletni strani in jih vrne v seznamu.
    Funkcija vrne seznam, v katerem posameznem element predstavlja odsek hmlt-ja s podatki za knjigo."""
    knjige = [knjiga.group(1).strip() for knjiga in re.finditer(vzorec_knjiga, vsebina)]
    return knjige

def zadetek(vzorec, ime_skupine, knjiga):
    """Funkcija poišče v html odseku za knjigu dan vzorec in poimenovanje skupine. Vrne zadetek, če ga pa ni vrne None."""
    zadetek = re.search(vzorec, knjiga).group(ime_skupine)
    return zadetek or None

def knjiga_v_slovar(knjiga):
    """Funkcija iz odseka hmtl besedila za posamezeno knjigo izlušči podatke o avtorju, naslovu dela, oceno in število volilcev, 
    ki je za knjigo glasovalo, da spada na seznam za obvezno čtivo. Vrne te podatke urejene v slovarju. """

    slovar = {
        skupina_naslov: zadetek(vzorec_naslov, skupina_naslov, knjiga),
        skupina_avtor: zadetek(vzorec_avtor, skupina_avtor, knjiga),
        skupina_ocena: float(zadetek(vzorec_ocena, skupina_ocena, knjiga)),
        skupina_stevilo_volilcev: int(zadetek(vzorec_stevilo_volilcev, skupina_stevilo_volilcev, knjiga).replace(",", ""))
    }

    return slovar

for stran in range(STEVILO_STRANI):
    """Zanka za vsako stran pokliče spletno stran, prebere njen html in ga shrani v mapo 'need-to-read', potem nazaj prebere to 
    pravkar shranjeno datoteko, naredi seznam knjig, nato pa v slovarji_knjig shrani slovar, ki predstavlja posamezno knjigo z zbranimi podatki."""
    
    prva_na_strani = stevec*STEVILO_KNJIG_NA_STRAN + 1
    zadnja_na_strani =  STEVILO_KNJIG_NA_STRAN*(stevec+1)
    url = f'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page={stevec+1}'
    stevec += 1
    datoteka = f'/need-to-read/{prva_na_strani}-{zadnja_na_strani}.html'
    orodja.shrani_spletno_stran(url, datoteka)

    vsebina = orodja.vsebina_datoteke(datoteka)
    knjige = html_v_knjige(vsebina) 

    for knjiga in knjige:
        slovarji_knjig.append(knjiga_v_slovar(knjiga))

#vse podatke, ki so urejeni v slovarji_knjig zapiše v .csv datoteko
orodja.zapisi_csv(slovarji_knjig, slovarji_knjig[0].keys(), 'knjige.csv')

#vse podatke, ki so urejeni v slovarji_knjig zapiše v .json datoteko
with open('knjige.json', 'w') as f:
    json.dump(slovarji_knjig, f, indent=2, ensure_ascii=True)

    
    