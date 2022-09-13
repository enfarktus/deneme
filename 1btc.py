import secp256k1 as ice
import random
print("1btcTARAMASON")
adresler = [line.split()[0] for line in open("btc1.txt",'r')]
adresler = set(adresler)
a=1
while(True):
 xx = random.randint(10069210371963397640889516,19999921037196339764088951659250242535245633416490421581207668153570251965137)
 addrc = ice.privatekey_to_address(0, True, xx)
 addru = ice.privatekey_to_address(0, False, xx)
 if addru in adresler or addrc in adresler :
  print("*************************Tebrikler***************")
  dosya = open("XXXX.txt", "a")
  dosya.write(str(xx) + " " + addru+ " " +addrc + "\n")
  dosya.close()

 xx1 = random.randint(20069210371963397640889516592502425352456334164904215812076681535702519651372,92369210371963397640889516592502425352456334164904215812076681535702519651372)
 addrc1 = ice.privatekey_to_address(0, True, xx1)
 addru1 = ice.privatekey_to_address(0, False, xx1)
 if addru1 in adresler or addrc1 in adresler:
  print("*************************Tebrikler***************")
  dosya = open("XXXX.txt", "a")
  dosya.write(str(xx1) + " " + addru1+ " " +addrc1+  "\n")
  dosya.close()
  
 xx2 = random.randint(92369210371963397640889516592502425352456334164904215812076681535702519651372,115269210371963397640889516592502425352456334164904215812076681535702519651372)
 addrc2 = ice.privatekey_to_address(0, True, xx2)
 addru2 = ice.privatekey_to_address(0, False, xx2)
 if addru2 in adresler or addrc2 in adresler:
  print("*************************Tebrikler***************")
  dosya = open("XXXX.txt", "a")
  dosya.write(str(xx2) + " " + addru2+ " " +addrc2+ "\n")
  dosya.close()
 else:
  print(str(a)+" "+str(xx)+ "\n" +str(xx1)+ "\n" +str(xx2)+ "\n")
 a+=1


