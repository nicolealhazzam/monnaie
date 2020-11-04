def rendreMonnaie(billets, montant):
    n = len(billets)
    trouver = [0] * n # creer un liste de n element
    for i in range(0,n,1): 
        while montant >= billets[i]: #test si le plus grand bill se trouve dans le montant
            montant = montant -  billets[i] # si le valeur est trouver dnas billets, donc enlever le.
            trouver[i] += 1 
    return trouver

def rendreMonnaieRec(billets,montant):
    n = len(billets)
    if n > 0:
        if montant > 0:
            if montant >= billets[0]: # test si le plus grand bill se trouve dans le montant
                existsNb = montant / billets[0]
                montant = montant -  billets[0] * int(existsNb) # si le valeur est trouver dnas billets donc enlever le.
                return [int(existsNb)] + rendreMonnaieRec(billets[1:],montant)
            else:
                return [0] + rendreMonnaieRec(billets[1:],montant)
    return [0]*(n)


"""
print(billets[-1:])
print(billets[:-1])
def removeMontant(i, montant):
    billets = [100000, 50000, 20000,10000,5000,1000]
    indexB = billets.index(i)
    LastindexB = billets.index(1000)
    newList = billets[indexB:LastindexB]
    print(newList)
    #if(ind > 0): ind = ind - 1
    if(montant >= i):
        #print(montant - i)
        if(montant/i >= 1):
            return montant
        else:
            #if()
            if(montant/i >= 1):
               return montant - (billets[indexB-1])
    else:
        return montant
"""

montant = 70000
billets = [100000, 50000, 20000,10000,5000,1000]
#Version liste compréhension
listComp = [ int(montant / i) if  montant >= i else 0 for i in billets ]

#execution
print(rendreMonnaie(billets, montant))
print(rendreMonnaieRec(billets, montant))
print(listComp)
