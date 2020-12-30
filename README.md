Repozitorij za projektno nalogo pri Programiranju 1 kot izbirnem predmetu v tretjem letniku Pedagoške matematike.

Analizirala bom podatke o prvih 3000 knjig iz spletne strani: https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once

# 3000 knjig, ki jih mora vsakdo prebrati

<b>Za vsako knjigo iz strani bom zajela:</b>
<ul>
  <li>naslov knjige,</li>
  <li>avtorja/avtorico,</li>
  <li>povprečno oceno knjige,</li>
  <li>število uporabnikov, ki je v volitvah pritrdilo, da morajo ljudje to knjigo obvezno prebrati</li>
 </ul>
 
 ## Delovne hipoteze
 S pomočjo analize podatkov želim izvedeti:
 <ul>
  <li>Kateri avtor ima največ knjig med izbranimi?</li>
  <li>Katera knjiga ima najboljšo in katera najslabšo oceno?</li>
  <li>Ali ima avtor knjige z najboljšo/najslabšo oceno tudi ostale knjige visoko ocenjene?</li>
  <li>Ali obstaja povezava med število ocen in povprečno oceno?</li>
  <li>Kako so knjige porazdeljene med ocenami?</li>
 </ul>

 <h2>Opis datotek v repozitoriju</h2>
 <ul>
  <li><b>orodja.py</b>: python datoteka, ki jo je pripravil profesor predmeta Programiranje 1, doc. dr. Matija Pretnar </li>
  <li><b>poberi_in_shrani_podatke.py</b>: program v pythonu, ki ob zagonu prebere spletno stran, izlošči podatke in jih shrani v .csv in .json datoteki</li>
  <li><b>knjige.csv</b>: csv datoteka, ki vsebuje naslovno vrstico in podatke vseh 3000 knjig. Datoteko dobimo ob pogonu poberi_in_shrani_podatke.py</li>
  <li><b>knjige.json</b>: json datoteka, ki vsebuje slovar podatkov o knjigah, vsaka knjiga je predstavljena s slovarjem, ki ima za ključe nadimek podatkov, za vrednosti pa ustrezen podatek za določeno knjigo. Datoteko dobimo ob pogonu poberi_in_shrani_podatke.py</li>
  <li><b>obdelava.ipynb</b>: ipynb datoteka, ki vsebuje analizo podatkov s pomočjo knjižnice pandas, ki jo ponuja python. 
 </ul>

