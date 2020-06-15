######Agregado por Josué#####
#Largo de lista
def len_recursive(lst):
    if not lst:
        return 0
    return aux_len_recursive(1 + len_recursive(lst[1::2]) + len_recursive(lst[2::2]))

def aux_len_recursive(lst):
    x=lst
    return x

#Largo de string
def str_length(string):
    if string == '': return 0
    return 1 + str_length(string[1:])


#Funcion recursiva para unir listas
def combine(a, b):
    alist = []
    if a == [] and b == []:
       return alist
    if a != [] and b == []:
       return alist + a
    if a == [] and b != []:
       return alist + b
    if a != [] and b != []:
       if a[0] <= b[0]:
          alist.append(a[0])
          alist = alist +  combine(a[1:], b)
       if a[0] > b[0]:
          alist.append(b[0])
          alist = alist +  combine(a, b[1:])
    return alist
        
#####Parte de Kenneth####
x=10010010
def aLista(n):
    if n < 10:
        return [n]
    return aLista(n//10) + [n%10]

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
    xLista.append(tercerxor)
    xListaTemp=[]
    xListaTemp.append(xLista[len_recursive(xLista)-1])
    xListaTemp.extend(xLista[:len_recursive(xLista)-2])

#En esta linea es necesaria una funcion recursiva que retorne el elemento dentro de la lista
#Por ese motivo estoy buscando una funcion recursiva que lo haga o hacerla yo mismo
    xListaTempStr="".join(str(printer(n)) for i in xListaTemp])combine(, xListaTemp)
    
    return xListaTempStr
#print(nextKey(x))

keyEnLista=[] #usa las funciones anteriores para generar una llave de contador elementos. x es la llave pasada a binario, contador es la
#cantidad de letras a encriptar o desencriptar
def keyGenerator(x,contador):
    if contador>0:
        keyEnLista.append(x)
        x=nextKey(x)
        return keyGenerator(x,contador-1)
    else:
        keyEnLista.append(x)
        return keyEnLista
print(keyGenerator (x,2))
