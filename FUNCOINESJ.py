#Linear feedback Shift Regidter
def LFSR(n):  
    Byte=[0,0,0,0,0,0,0,0]
    return n
    



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


#Seccion para convertir numero a lista

#Largo de lista
def len_recursive(lst):
    if not lst:
        return 0
    else:
        return aux_len_recursive(1 + len_recursive(lst[1::2]) + len_recursive(lst[2::2]))

def aux_len_recursive(lst):
    lst=n
    return aLista1(n)

#Convertir numero a lista
def aLista1(n):
    c=length(n)
    return aux_aLista(n,c)

def aLista(n,c):
    if n < 10:
        return [n]
    return aux_aLista((n//10) + [n%10],c-1)

def aux_aLista(n,c):
    if c == 1 and (n > 10 or length(n) >= aux_len_recursive(n)):
        return (LFSR(n))
    else:
        return LFSR((n//10) + [n%10],c-1)
    if c != 1 and (n < 10 or (length(n)) >= laux_len_recursive(n)):
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

def decryptList(lst):
    if len(lst) != 0:
        decryptElement(lst)
        print(lst[0])
        return [lst.pop(0)] + decryptList(lst)
        return []

def decryptElement(lst):
    if lst==[]:
        n=lst.pop(0)
        return n
    if len(lst) == 1:
        n=lst.pop(0)
        print (lst)
    if len(lst) != []:
        print(lst[0],end='')
        n=lst.pop(0)
        print (decryptElement(lst))
            
def extractor(lst):
    return lst


def printer(n):
    return n



#Devuelve string reverso        
def reverse(text):
    text=str(text)
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:])+text[0]
    return(reverse(text))

def len_recursive(lst):
    if not lst:
        return 0
    return aux_len_recursive(1 + len_recursive(lst[1::2]) + len_recursive(lst[2::2]))

def aux_len_recursive(lst):
    x=lst
    return x


def replace(thelist,a,b):
    #base case 1: thelist is empty
    if thelist==[]:
        return thelist
    #case 1: the first character is a
    elif thelist[0] == a:
        thelist[0] = b
    return thelist[:1] + replace(thelist[1:], a, b)




def b_toD(n):
    if length(n)!=1:
        return b_toD(int(n,2))
    return aux_b_toD(n)

def binaryToDecimal(n):
    n=str(n)
    return int(n,2)
