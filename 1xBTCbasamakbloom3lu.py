import secp256k1 as ice
import random
from pathlib import Path
from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate

mys = Path(__file__).resolve()
fil = 'found.txt'
myselff = Path(__file__).resolve()
ress = 'btc.bf'

with open(ress, "rb") as fp:
    bloom_filter = BloomFilter.load(fp)

a=0
bx = 0x400000000000000000000000000000000000000000000000000000000000000
#bx = random.randint(0x100000000000000000000000000000000000000000000000000000000000000,0xfffff0000000000000000000000000000000000000000000000000000000000)
xx =  bx
yx = bx
zx = bx 
while(True):

     xx+= 0x10000000000000
     xx1= xx+0xfffffffffffff
     
     yx+= 0x10000000000000000000000000000000000
     yx1= yx+0xffffffffffffffffffffffffffffffffff
         
     zx+= 0x1000000000000000000000000000000000000000000000000
     zx1= zx+0xffffffffffffffffffffffffffffffffffffffffffffffff

     privh = (hex(xx))
     privh1 = (hex(yx))
     privh2 = (hex(zx))
     print("btcb:", str(a), "temel:", privh2, end='\r')
     a+=1
     for x in range(5000):
       xx2 = random.randint(xx,xx1)
       addrc = ice.privatekey_to_address(0, True, xx2)
       addru = ice.privatekey_to_address(0, False, xx2)
       if addrc in bloom_filter or addru in bloom_filter:
           print ("winner!!!!!!!!!!!!!!!!", str(xx2))
           g=open(fil,"a")
           g.write("\n" + addrc +" "+addru)
           g.write("\n" + str(xx2))      
           g.close()

       yx2 = random.randint(yx,yx1)
       addrc1 = ice.privatekey_to_address(0, True, yx2)
       addru1 = ice.privatekey_to_address(0, False, yx2)
       if addrc1 in bloom_filter or addru1 in bloom_filter:
           print ("winner!!!!!!!!!!!!!!!!", str(yx2))
           g=open(fil,"a")
           g.write("\n" + addrc1 +" "+addru1)
           g.write("\n" + str(yx2))      
           g.close()

       zx2 = random.randint(zx,zx1)
       addrc2 = ice.privatekey_to_address(0, True, zx2)
       addru2 = ice.privatekey_to_address(0, False, zx2)
       if addrc2 in bloom_filter or addru2 in bloom_filter:
           print ("winner!!!!!!!!!!!!!!!!", str(zx2))
           g=open(fil,"a")
           g.write("\n" + addrc2 +" "+addru2)
           g.write("\n" + str(zx2))      
           g.close()

