# Example recordings

## Decode several hours of data at 433.92MHz with rtl_433
```
bunzip2 -c dump_cut.complex16u.bz2 | rtl_433 -Y level=-27 -r -
```

## Decode recorded Kedsum datagram with rtl_433
```
rtl_433 -Y level=-27 -r kedsum.complex16u
```

## Decode crafted Kedsum datagram with rtl_433
```
rtl_433 -Y level=-27 -r yard.complex16u
```

