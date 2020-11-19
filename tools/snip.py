import math

file = "../recordings/dump.complex16u"
outfile = "../recordings/dump_cut.complex16u"

squelch = 0


with open(file, "rb") as f:
    with open(outfile, "wb") as of:
        while (byte := f.read(2)):
            i = byte[0] - 128
            q = byte[1] - 128
            s = math.sqrt(i*i+q*q)
            if s >= 4:
                squelch = 2500
            if squelch > 0:
                squelch = squelch - 1
                of.write(byte)

