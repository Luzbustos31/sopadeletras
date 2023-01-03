import csv
import string


class Obtener_datos :
    def __init__(self):          
        pass
                          
    def obtener_datos_usuario (self):               
        
        def func_datos (texto,func):        
            dato = input (texto)
            while not func (dato) :
                dato = input (texto)
            return dato

        def validar_archivo(nombre):
            try:
                with open (nombre) as file:
                    print ("abrimos archivo")
                    return True
            except:
                print ("no se pudo abrir")
                return False 

        def obtener_datos_tablero(nombre_usuario):                    
            return len (nombre_usuario) < 40

        nombre_usuario= func_datos("Ingrese su nombre de usuario: ", obtener_datos_tablero)
        print ("Jugador/ra: ", nombre_usuario)
        nombre_archivo = str (func_datos ("Ingrese el nombre del archivo (menor a 30 caracteres): ", validar_archivo))
        return nombre_usuario, nombre_archivo                                   
                      


class Tablero:
    def __init__(self,nombre_archivo):
        self.matriz = []
        self.diccionario={}
        self.nombre_archivo=nombre_archivo
    
        
    def crear_cuadricula (self):                                                             
        with open(self.nombre_archivo + ".csv" ,newline= "") as File:        
            reader = csv.reader(File, delimiter=",", quotechar=",",
                                quoting=csv.QUOTE_MINIMAL)
            for x in reader:
                self.matriz.append(x)
                separador = "|"                                     
                print (separador.join(map(str,x)))
                
        with open(self.nombre_archivo + '_solucion.csv', newline= "") as File:       
            reader = csv.reader(File)
            next(reader)
            for linea in reader:
                self.valores=[]
                for valor in linea:
                    self.valores.append(valor)
                self.diccionario[self.valores[0]]=self.valores[1],self.valores[2],self.valores[3],self.valores[4]
                self.dicci_solo_palabras=self.diccionario.keys()
                    
         
            
    def lista_palabras_dic(self):               #palabras solas en el diccioario
        self.palabras_dicc= self.dicci_solo_palabras
        return self.palabras_dicc                     
                

    def verificar_palabra(self,palabra):    
        if palabra in self.diccionario:
            return True
        else:
            return False   
    

    def imprimir(self):
        separador = "|"
        for x in self.matriz:
            print (separador.join(map(str,x)))



    def mayusculas(self,palabra):                                   
        
        valores = self.diccionario[palabra] 
        
        if int(valores[0]) == int(valores[2]):
            for i in range (len(palabra)):
                x= int(valores[0])
                y= int(valores[1])
                self.matriz[x][y+i]= palabra[i].upper()
        else:
            for i in range (len(palabra)):
                x= int(valores[0])
                y= int(valores[1])
                self.matriz[x+i][y]= palabra[i].upper()
        return self.matriz
        


class Jugador:                                  
    def __init__(self,nombre_usuario,puntaje):
        self.nombre_usuario = nombre_usuario   
        self.puntaje = puntaje

    def sumar_punto (self):
        self.puntaje= self.puntaje +1
        return (self.puntaje)                         
                                                              

    def __str__(self):  
        return "El jugador " + self.nombre_usuario + " finalizó el juego con " + str (self.puntaje) + " puntos"


class Juego:                                              
    def __init__(self,nombre_usuario, nombre_archivo):
        self.nombre_usuario = nombre_usuario
        self.nombre_tablero = nombre_archivo
        self.jugador = Jugador(nombre_usuario,0)
        self.tablero = Tablero(nombre_archivo)
                 

    def jugar(self):                              
        print (self.tablero.crear_cuadricula())
        palabra= ("Ingrese la palabra encontrada (o fin para terminar el juego): ")                      
        self.tablero.verificar_palabra(palabra)
        palabras_encontradas=[]                                                                      
        
        while len(palabras_encontradas) != len (self.tablero.lista_palabras_dic()):
            palabra= input ("Ingrese la palabra encontrada (o fin para terminar el juego): ")              #PIDE UNA VUELTA MAS DEL INPUT PERO NO HACE NADA                                                                          
            if palabra == "fin":
                ordenar_alf = self.tablero.lista_palabras_dic() - palabras_encontradas
                print ("Las palabras que no fueron encontradas son: ",sorted(ordenar_alf))
                break    
            if self.tablero.verificar_palabra(palabra) == True:                            
                palabras_encontradas.append(palabra) 
                print ("LA PALABRA ESTABA EN EL TABLERO!!! sigamos..")
                self.tablero.mayusculas(palabra)  
                self.tablero.imprimir()                                                                 
                puntos =self.jugador.sumar_punto()
                                                                                                                    
            else: 
                print ("La palabra ingresada no se encuentra en la sopa de letras")
                
        else:
            print ("Encontraste todas las palabras, FELICITACIONES!!!")        
        print ("Palabras encontradas: ", (palabras_encontradas))
        print (Jugador(self.nombre_usuario,puntos).__str__())                                                                                                                  
                                                                                   
                                                
                                            

class Programa:
    def main ():
        nombre_usuario, nombre_archivo= Obtener_datos().obtener_datos_usuario()
        jugando = Juego(nombre_usuario,nombre_archivo)
        jugando.jugar()
        
    main()        
    
    
                                
        

