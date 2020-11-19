# was_funkt_denn_da

https://github.com/merbanan/rtl_433/blob/master/src/devices/kedsum.c

Settings:
  | Noise           | 0.3 |
  | Center          | 0.5 |
  | Samples/Symbol  | 100 |
  | Error Tolerance | 5   |
  | Modulation      | ASK |
  | Bits/Symbol     | 1   |
  | Pause           | 19  |

Decoding:
  1. Invert
  2. Morse Code (1,8,1) 

temp = (low + mid * 16 + hi * 256 - 900) * 0.1
hum = low + high * 16


rtl_433 output:
model      : Kedsum Temperature & Humidity Sensor   ID        : 154
Channel    : 2            Battery   : LOW           Flags2    : 8
Temperature: 23.61 C      Humidity  : 53 %          Integrity : CRC

74.50 F = 23.61 C


# installation

pip install crccheck
