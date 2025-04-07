from def0704 import v_koni
from def0704 import v_sil
from def0704 import v_top

r1 = int(input("koni r"))
h1 = int(input("koni h"))
r2 = int(input("sil r"))
h2 = int(input("sil h"))

koni = v_koni(r1,h1)
sil = v_sil(r2,h2)

top = v_top(koni,sil)

print (round(top,2))