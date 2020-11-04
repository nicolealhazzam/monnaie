def toutRendreMonnaie(billets, montant):
    n = len(billets)
    trouver = [0] * n # creer un liste de n element
    initMontant = montant
    for i in range(0,n,1): 
        while montant >= billets[i]: #test si le plus grand bill se trouve dans le montant
            montant = montant -  billets[i] # si le valeur est trouver dnas billets, donc enlever le.
            trouver[i] += 1
        montant = initMontant 
    return trouver

def toutRendreMonnaieRec(billets,montant):
    n = len(billets)
    if n > 0:
        if montant > 0:
            if montant >= billets[0]: # test si le plus grand bill se trouve dans le montant
                existsNb = montant / billets[0]
                #montant = montant -  billets[0] * int(existsNb) 
                return [int(existsNb)] + toutRendreMonnaieRec(billets[1:],montant)
            else:
                return [0] + toutRendreMonnaieRec(billets[1:],montant)
    return [0]*(n)

montant = 70000
billets = [100000, 50000, 20000,10000,5000,1000]
listComp = [ int(montant / i) if  montant >= i else 0 for i in billets ]
print(toutRendreMonnaie(billets, montant))
print(toutRendreMonnaieRec(billets, montant))
print(listComp)