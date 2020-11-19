---

revealOptions:
  transition: fade
  title: Backup
  animate: true
  controls: true
  progress: true

---

# Was funkt denn da

---

## Elektromagnetisches Spektrum

<img alt="EM-Spektrum" src="images/EM-Spektrum.svg"><br>
<a style="font-size: 0.5em" title="Matt, CC BY-SA 2.5 &lt;https://creativecommons.org/licenses/by-sa/2.5&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg">Quelle: https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg</a>

---

## Drahtlose Kommunikation

  * Radio, TV (AM, FM, DAB, DVB)
  * Mobiltelefon (GSM, LTE etc.)
  * Wireless LAN (WiFi)
  * Blutetooth
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

## Interssante Frequenzbereiche

<img alt="EM-Spektrum" src="images/EM-Spektrum-arrow.svg"><br>
  * 100 MHz: FM-Radio
  * 434 MHz: Thermometer, Autoschlüssel etc.
  * 868 MHz: WMBUS, Alarmanlagen, etc.
  * 1090 MHz: ADS-B (Luftfahrzeugtransponder)

<a style="font-size: 0.5em" title="Matt, CC BY-SA 2.5 &lt;https://creativecommons.org/licenses/by-sa/2.5&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg">Quelle: https://commons.wikimedia.org/wiki/File:EM-Spektrum.svg</a>

---

# Empfang

----

## Hardware

  * rtl-sdr
  * hackrf one
  * Antenne

----

## Software

  * GQRX
  * rtl_433
  * urh
  * dump_1090
  * gnuradio
