#f = open("prueba.txt", "a+")
#f.write("prueba")
#f.close()

def xor(a,b):
    if a==1 and b==1:
        return 0
    if a==0 and b==0:
        return 0
    else:
        return 1

def rotarLista(l, n):
    return B[-n:] + B[:-n]

'''funcion que busque un digito en la lista a y retorne su posicion (index)'''
'''funcion que busque esa posicion en la lista rotada y retorne su digito '''

#def convierteEnLista(x):
#    entrada=list(x)
#    print(entrada)    <-----esta funcion es una prueba

B=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
resultado=[]
resultado2=[]
def encrypt(x, llave):
    return B[(B.index(x)+llave)%len(B)]
#x es la letra a encriptar con una llave, encrypt("a",1) deberia dar b
llave=[1,2,3,4,5,6]

def encryptWordbyLetter2(word, llave):
    entrada=list(word)
    
    if len(entrada)>1:
        resultado.append(encrypt(entrada[0],llave[0]))
        return encryptWordbyLetter2(entrada[1:],llave[1:])
    else:
        resultado.append(encrypt(entrada[0],llave[0]))
        resultadoStr="".join(resultado)
        return resultadoStr
#encripta palabras letra por letra con una llave del tamano de la palabra. word es la palabra y llave la letra
#print (encryptWordbyLetter2("wep",llave))

def cd (n):
    if n<10:
        return 1
    else:
        return 1+cd(n//10)      

def decrypt(x, llave):
    return B[(B.index(x)-llave)%len(B)]
#desencripta una letra x con una llave
llave=[1,2,3,4,5,6]
def decryptWordbyLetter(encrypted,llave):
    entrada=list(encrypted)
    if len(entrada)>1:
        resultado2.append(decrypt(entrada[0],llave[0]))
        return decryptWordbyLetter(entrada[1:],llave[1:])
    else:
        resultado2.append(decrypt(entrada[0],llave[0]))
        resultado2Str="".join(resultado2)
        return resultado2Str
#desencripta palabras recursivamente letra por letra
#print(decryptWordbyLetter("igs",llave))

f = open("prueba.txt","r")
mensaje = f.read()
mensajeSrt="".join(mensaje)
mensajeL=list(mensajeSrt)
#print(mensajeL)
f.close()
#print(llave)
#abre un archivo .txt existente en la misma carpeta que el .py y lo "importa" y lo convierte en lista para poder ser utilizado por el
#algoritmo de encriptado o desencriptado
print(decryptWordbyLetter("qtxigg",llave))
#print(encrypt("a",1))
#print(encryptWordbyLetter2(mensaje,llave))