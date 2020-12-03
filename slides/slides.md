---

revealOptions:
  transition: fade
  title: Backup
  animate: true
  controls: true
  progress: true

---

# Was funkt denn da?

----

<table>
  <tr>
    <td style="text-align: center">
      <img src="" width="150"/><br>
      Daniel Zerlett<br>
      Software Architect<br>
      <br>
      Tüftler, Maker, Hacker und
      Funkamateur (DL1ZD)<br>
    </td>
    <td width="50">
    </td>
    <td style="text-align: center">
      Wolfram Quester<br>
      Physiker, Product Owner, Scrum Master </br>
      <br>
      Segler, Bastler, Mädchen für alles
    </td>
  </tr>
</table>

---

## Elektromagnetisches Spektrum

<img alt="EM-Spektrum" src="images/EM-Spektrum.svg"><br>
<a style="font-size: 0.5em" title="Matt, CC BY-SA 2.5 &lt;https://creativecommons.org/licenses/by-sa/2.5&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg">Quelle: https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg</a>


----

## Meilensteine der Nachrichtentechnik

  * 1820: Entdeckung des Elektromagnetismus
  * 1888: 10 Meter weite Übertragung (H. Hertz)
  * 1901: Marconi morst über den Atlantik
  * 1906: Erste Übertragung eines Unterhaltungsprogramms zu Weihnachten
  * 1912: Untergang der Titanic
  * 1920er: Erste Fernsehübertragung
  * 1950: Funkmeldeempfänger ("Pager") in USA
  * 1953: NTSC-Farbfernsehen
  * 1958: A-Netz (erstes analoges deutsches Funktelefonnetz)
  * 1992: D-Netz
  * ...


---

## Drahtlose Kommunikation

  * Radio, TV (AM, FM, DAB, DVB)
  * Mobiltelefon (GSM, LTE etc.)
  * Betriebs- und Seefunk
  * Satellitennavigation
  * Wireless LAN (WiFi)  
  * Bluetooth
  * IoT (Zigbee, Z-Wave, WMBus, BLE...)
  * ...?

---

# Anwendungen

  * Funkthermometer
  * Wetterstationen
  * Funksteckdosen
  * Garagentoröffner
  * Autoschlüssel
  * Reifendruckkontrollsysteme
  * ADS-B (Flugzeugtransponder)
  * Radiosonden (Wetterballons)

----

# Gemeinsamkeiten der genannten Anwendungen

  * Die Kommunikation dieser Protokolle ist Unicast/Simplex
  * meistens Amplitudenmodulation (ASK)
  * ...oder Frequenzmodulation (FSK)
  * UHF-Band
  * kurze Nachrichten
  * seltenst verschlüsselt
  * einfach&#8482; zu empfangen &#9758;&#9786;
  
----

## ASK/FSK

<img src="images/ask-fsk.png">

----

## Interessante Frequenzbereiche

<img alt="EM-Spektrum" src="images/EM-Spektrum-arrow.svg"><br>
  * 100 MHz: FM-Radio
  * 434 MHz: Thermometer, Autoschlüssel etc.
  * 868 MHz: WMBUS, Alarmanlagen, etc.
  * 1090 MHz: ADS-B (Luftfahrzeugtransponder)

<a style="font-size: 0.5em" title="Matt, CC BY-SA 2.5 &lt;https://creativecommons.org/licenses/by-sa/2.5&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg">Quelle: https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg</a>

---

# Hardware

Welche Geräte/Ausrüstung brauche ich um diese Signale empfangen zu können

#### ❓❓❓

----

## rtl-sdr

<img src="images/rtl_sdr_lowcost.jpg" height="250"><br>

  * ca. 25€
  * max. Bandbreite 2.4MS/s
  * RX 24MHz bis 1766MHz

----

<img src="images/rtl_sdr_premium.jpg" height="350"><br>

  * ca. 40€
  * max. Bandbreite 3.2MS/s
  * RX 24MHz bis 2.2GHz mit Lücke bei ca. 1GHz

----

## Antennen

<img src="images/433MHz_dipole.jpg" height="350"><br>
  
  * Eigenbau 433 MHz Dipol

----

## Antennen

<img src="images/1090MHz_groundplane.jpg" height="300"><br>

  * Eigenbau 1090 MHz Groundplane

----

## HackRF One

<img src="images/hackrf_one.jpg" height="200"><br>

  * ca. 300€
  * halbduplex
  * 1MHz bis 6GHZ 😀
  * SDR mit 20MS/s

----

## YardStick one

<img src="images/yard_stick_one.jpg" height="200"><br>

  * ca. 99€
  * halbduplex
  * High-Level RF-Interface, kein SDR (CC1111)
  * TX 300-348 MHz, 391-464 MHz und 782-928 MHz
  * ASK, OOK, GFSK, 2-FSK, 4-FSK, MSK
  * max. 500kbps

---

## Software

Welche Software brauche ich um diese Signale empfangen und decodieren zu können

#### ❓❓❓

----

## GQRX

<img src="images/gqrx.jpg" height="350">

  * Einfacher SDR-Empfänger mit GUI
  * Schöne Spektral- und Wasserfallansicht
  * Demodulatoren für AM/FM/SSB etc.

Note: FM-Radio empfangen, lokaler Stick (blau)

----

## rtl_433

<img src="images/rtl_433.png" height="350">

  * Konsolenprogramm
  * https://github.com/merbanan/rtl_433
  * Empfängt viele Wetterstationen und RDK-Systeme etc.

Note:
 * Thermometer und Reifen live
 * Playback
 * raspberry Stick

----

### Warum packt der sein Thermometer in den Kühlschrank?

oder

### Gut dass es draußen kälter ist als drinnen!

----

## urh

<img src="images/urh.png" height="350">

  * "Investigate wireless protocols like a boss"
  * https://github.com/jopohl/urh

Note: Thermometer manuell decodieren

----

## selber senden?

  * Bitte Gesetze beachten!
  * Replay-Attacke/Spoofing mit Yard Stick One
  * https://github.com/b00lduck/433mhz_thermo_spoof

----

## dump_1090

  * ADSB-Signale empfangen und decodieren
  * https://github.com/antirez/dump1090

Note: mit raspberry und website

----

## gnuradio-companion

<img src="images/gnuradio-companion.png" height="350">

Note: FM TX
