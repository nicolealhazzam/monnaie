def factorial(n):
   if n == 0: # Base case
      return 1
   else:
      return n * factorial(n - 1) # Recursive call

      
n = 3
print("Factorial of", n, "is", factorial(n))
def lstcomp(caisse,montant,m,coinsUsed):
   for ce in range(montant+1):
      coinCount = ce
      newCoin = 1
      for j in [c for c in caisse if c <= ce]:
            if m[ce-j] + 1 < coinCount:
               coinCount = m[ce-j]+1
               newCoin = j
      m[ce] = coinCount
      coinsUsed[ce] = newCoin
   return m[montant]

def afficher(coinsUsed,montant):
   coin = montant
   while coin > 0:
      c= coinsUsed[coin]
      print(c)
      coin = coin - c


montant = 150000
caisse = [100000,50000,20000,10000,5000,1000,500,250]
coinsUsed = [0]*(montant+1)
coinCount = [0]*(montant+1)

print("pour",montant,"besoin")
print(lstcomp(caisse,montant,coinCount,coinsUsed),"monnaie(s)")
print("sont")
afficher(coinsUsed,montant)


def toutrendreM(res, caisse, h, sum, montant):
    if sum == montant:
       for c in caisse:
        count = res.count(c)
        print(c, ":", count)
    if sum > montant:
        return
    for value in caisse:
        if value >= h:
            copy = res[:]
            copy.append(value)
            toutrendreM(copy, caisse, value, sum + value, montant)
'''
def afficher(res, caisse):
   
    for c in caisse:
        count = res.count(c)
        print(c, ":", count)
    print("")'''

res = []
caisse = [100000,50000]
montant=50000
toutrendreM(res, caisse, 0, 0,montant)
