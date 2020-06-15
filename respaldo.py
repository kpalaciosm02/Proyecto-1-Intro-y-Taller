#Linear feedback Shift Regidter
def LFSR(n):  
    Byte=[0,0,0,0,0,0,0,0]

    



def xor(L):
#x = digito de la derecha  n = digito de la izquierda
    if (len(L)) % 2 == 0:
        x= L[(len(L)-2)]
        n= L[len(L)]
        return (aLista(x^n))
    else:
        x= L[(len(L)-2)]
        n= L[(len(L)-3)]
        return (aLista(x^n))


#Funcion not para obtener xnor
def xnor(xor):
    if xor == 0:
        return 1
    else:
        return 0

#binary to decimal
def n_toBase(n,base):
    string_conversion = '0123456789ABCDEF'

    if n < base:
        return string_conversion[n]  
    else:
        return n_toBase(n//base,base) + string_conversion[n % base]


#Decimal to Binary
def Dec_B(n): 
    if n == 0: 
        return 0
    if n < 0:
        return Dec_B(n*-1)
    else: 
        return (n % 2 + 10 * Dec_B(int(n // 2)))





def op(L):
    Byte=[0,0,0,0,0,0,0,0]
    L=[()]


#Convierte lista a numero 
def aNumero(n):
    if n < 10:
        return n
    else:
        return aNumero(n // 10)+[n%10]


#Convierte numero a lista
def aLista(n,c=len(n)):
    if n < 10:
        return [n]
    return aux_aLista((n//10) + [n%10],c-1)

def aux_aLista(n,c):
    if c == 1 and (n > 10 or length(n) >= len(n)):
        return (LFSR([n]))
    else:
        return LFSR((n//10) + [n%10],c-1)
    if c != 1 and (n < 10 or (length(n)) >= len(n)):
        return [n]
    else:
        return aux_aLista((n//10) + [n%10],c-1)

    
#Extractor de bits

    



























#Number length
def length(n):
    if n < 0:
        return (length_neg(n))
    else:
        if n < 10:
            return 1
        if n > 9:
            count=1
            return 1+(count*(length(n // 10)))

def length_neg(n):
    if n > -9:
        return 1
    if n != 0 and n < 0:
        countneg= -1
        return (1-(countneg*(length(n // -10))))     


#Funcionan    
def desencriptarLista(lista):
    if len(lista) != 0:
        desencriptarPrimerElemento(lista)
        print(lista[0])
        return [lista.pop(0)] + desencriptarLista(lista)
    return []

def desencriptarPrimerElemento(lista):
    if lista==[]:
        n=lista.pop(0)
        return n
    if len(lista) == 1:
        n=lista.pop(0)
        print (lista)
    if len(lista) != []:
        print(lista[0],end='')
        n=lista.pop(0)
        print (desencriptarPrimerElemento(lista))
            
def desencriptarLista(lista):
    if len(lista) != 0:
        desencriptarPrimerElemento(lista)
        print(lista[0])
        return [lista.pop(0)] + desencriptarLista(lista)
        return []        








#Devuelve string reverso        
def reverse(text):
    text=str(text)
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:])+text[0]
    return(reverse(text))















