#x="eyxdlsm"
def xor(a,b):
    if a==1 and b==1:
        return 0
    if a==0 and b==0:
        return 0
    else:
        return 1

def rotarLista(l, n):
    return B[-n:] + B[:-n]

B=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
resultado=[]
resultado2=[]

def encrypt(x, llave):
    print(llave)
    return B[(B.index(x)+llave)%len(B)]
    
#llave=[1,2,3,4,5,6]

def encryptWordbyLetter2(word, llave):
    entrada=list(word)
    
    if len(entrada)>1:
        resultado.append(encrypt(entrada[0],llave[0]))
        return encryptWordbyLetter2(entrada[1:],llave[1:])
    else:
        resultado.append(encrypt(entrada[0],llave[0]))
        resultadoStr="".join(resultado)
        return resultadoStr

def cd (n):
    if n<10:
        return 1
    else:
        return 1+cd(n//10)      

def decrypt(x, llave):
    return B[(B.index(x)-llave)%len(B)]
#desencripta una letra x con una llave
#llave=[1,2,3,4,5,6]
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

#print(decryptWordbyLetter("qtxigg",llave))



def aLista(x):
    if not isinstance(x, list):
        if x < 10:
            return [x]
        return aLista(x//10)+[x%10]
    else:
        return x

#xLista=aLista(llave)

def nextKey(x):
    #esta funcion solo genera apartir de la llave x en binario, las siguientes llaves a utilizar
    #^ es el simbolo para xor predeterminado en python
    xLista=aLista(x)
    xLista=[0]*(8-len(xLista))+xLista
    primerxor=xLista[7]^xLista[5]
    segundoxor=primerxor^xLista[3]
    tercerxor=segundoxor^xLista[2]
    
    xListaTemp=[]
    xListaTemp.append(tercerxor)
    xListaTemp.extend(xLista[:-1])
    xListaTempStr="".join([str(i) for i in xListaTemp])
    #xNum=int(xListaTempStr)
    return xListaTemp

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

def encryptFinal(x,llave):
    llaveBin=Dec_B(llave)
    
    yList=keyGenerator(llaveBin,len(x)) #llaveBin="0"*(8-len(llaveBin))+llaveBin
    y="".join([str(i) for i in yList])
    #print(yList)
    #print(y)
    llave2=quitaListas(yList)
    #print(llave2)
    llave2Dec=convLlaveDec(llave2)
    return encryptWordbyLetter2(x,llave2Dec)
def decryptFinal(x,llave):
    llaveBin=Dec_B(llave)
    
    yList=keyGenerator(llaveBin,len(x)) #llaveBin="0"*(8-len(llaveBin))+llaveBin
    y="".join([str(i) for i in yList])
    #print(yList)
    #print(y)
    llave2=quitaListas(yList)
    #print(llave2)
    llave2Dec=convLlaveDec(llave2)
    return decryptWordbyLetter(x,llave2Dec)
'''llaveB=10010010
yList=keyGenerator(llaveB,len(x))    #error'''

llaveCompBin=[]
def quitaListas(l):
    if len(l)==1:
        llaveCompBin.append(int("".join(str(i) for i in l[0])))
        return llaveCompBin
    else:
        llaveCompBin.append(int("".join(str(i) for i in l[0])))
        return quitaListas(l[1:])

def binaryToDecimal(n):
    n=str(n)
    return int(n,2)
llaveDec=[]
def convLlaveDec(llaveCompBin):
    if len(llaveCompBin)==1:
        llaveDec.append(binaryToDecimal(llaveCompBin[0]))
        return llaveDec
    else:
        llaveDec.append(binaryToDecimal(llaveCompBin[0]))
        return convLlaveDec(llaveCompBin[1:])
#llaveBin=(keyGenerator(10010010,len(x)))
#llaveBinEnteros=quitaListas(llaveBin)
#print(convLlaveDec(llaveBinEnteros))
#print (llaveBinEnteros)
#print(llaveBin)
def Dec_B(n): 
    if n == 0: 
        return 0
    if n < 0:
        return Dec_B(n*-1)
    else: 
        return (n % 2 + 10 * Dec_B(int(n // 2)))
#print(encryptFinal(x,15))

'''llaveBin=Dec_B(155)
llavePrueba=keyGenerator(llaveBin,7)
print(llavePrueba)'''
#print (encryptWordbyLetter2(x,))
#print(keyGenerator(10010010,8))
#llaveFinal=[146, 201, 228, 114, 57, 156, 78]
print(decryptFinal("eyxdlsm",15))
#print(Dec_B(5))