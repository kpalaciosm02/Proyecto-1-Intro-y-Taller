x=10010010
xLis=[1,0,0,1,0,0,1,0]
def aLista(x):
    if not isinstance(x, list):
        if x < 10:
            return [x]
        return aLista(x//10)+[x%10]
    else:
        return x

xLista=aLista(x)
#sucesion de xor para obtener el siguiente digito
#primerxor=xLista[7]^xLista[5]
#segundoxor=primerxor^xLista[3]
#tercerxor=segundoxor^xLista[2]

def nextKey(x):
    #esta funcion solo genera apartir de la llave x en binario, las siguientes llaves a utilizar
    #^ es el simbolo para xor predeterminado en python
    xLista=aLista(x)
    primerxor=xLista[7]^xLista[5]
    segundoxor=primerxor^xLista[3]
    tercerxor=segundoxor^xLista[2]
      #10010010 100100101
    xListaTemp=[]
    xListaTemp.append(tercerxor)
    xListaTemp.extend(xLista[:-1])
    xListaTempStr="".join([str(i) for i in xListaTemp])
    #xNum=int(xListaTempStr)
    return xListaTemp
#print(nextKey(x))

keyEnLista=[] #usa las funciones anteriores para generar una llave de contador elementos. x es la llave pasada a binario, contador es la
#cantidad de letras a encriptar o desencriptar
def keyGenerator(x,contador):
    if contador>1:
        keyEnLista.append(aLista(x))
        
        x2=nextKey(x)
        
        return keyGenerator(x2,contador-1)
    else:
        keyEnLista.append(x)
        return keyEnLista
print(keyGenerator (x,8))
#print (nextKey(xLis))

