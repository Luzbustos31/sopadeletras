
import random
import string
import csv


class Generar_tablero:
    def __init__(self,N, diccionario, tablero):
        self.N= N
        self.diccionario= diccionario
        self.tablero = tablero
    
    def verificar_ubicacion(self,len_palabra, x_inicio, y_inicio,orientacion):
        if orientacion == True:
            for i in range (len_palabra):
                if self.tablero [x_inicio + i][y_inicio] != -1:
                    return False
        if orientacion == False:
            for i in range (len_palabra):
                if self.tablero [x_inicio][y_inicio + i] != -1:
                    return True
    
    def generar (self,lista_palabras):  
        self.tablero = []
        self.diccionario = {}
        i= 0
        j= 0
        for lista in range (0, self.N):
            self.tablero.append ([])
        for fila in range (0, self.N):
            for columna in range (0,self.N):
                    self.tablero[columna].append(-1)


        for palabra in  (lista_palabras):                   
            x_inicio = random.randrange(0, self.N-len(palabra))
            y_inicio = random.randrange(0,self.N-len(palabra))
            orientacion = random.choice([True, False])
            while self.verificar_ubicacion (len(palabra),x_inicio,y_inicio,orientacion) == False:   
                x_inicio = random.randrange(0, self.N-len(palabra))
                y_inicio = random.randrange(0,self.N-len(palabra))
            if orientacion == True:
                self.diccionario [palabra]={"x_inicio":x_inicio, "y_inicio":y_inicio,"x_final":x_inicio +len(palabra)-1,"y_final":y_inicio}
                for i in range (len(palabra)):
                    self.tablero [x_inicio + i][y_inicio] = palabra [i]
            if orientacion == False:
                self.diccionario [palabra]={"x_inicio":x_inicio, "y_inicio":y_inicio,"x_final":x_inicio ,"y_final":y_inicio+len(palabra)-1}
                for i in range (len(palabra)):
                    self.tablero [x_inicio][y_inicio + i] = palabra [i]
    

        for i in range (0,self.N):
            for j in range (0,self.N):
                if self.tablero [i][j] == -1:
                    self.tablero [i][j] = random.choice(string.ascii_lowercase)
                                        
        separador = "|"
        for x in self.tablero:
            print (separador.join(map(str,x)))
        return self.diccionario, self.tablero
        

class Obtener_datos:
    def __init__(self) -> None:
        pass               
                                          

    def obtener_datos_usuario (self):
        def func_datos (texto,func):       
            dato = input (texto)
            while not func (dato) :
                dato = input (texto)
            return dato
        def validar_N (num):                         
            return int (num) >= 15

        N = int (func_datos ("Ingrese un numero (mayor a 15 y menor a 30): ", validar_N))
        def validar_palabra (palabra):
            if len (palabra) > N /3:
                print ("LA PALABRA ES MUY LARGA")
            return len (palabra) <= N /3
        
        diccionario = []
        i= 0
        cant = int (N / 3)
        print ("Ingrese", int (cant) -1, "palabras de hasta", int (cant), "letras(o la palabra fin para terminar) ")
        while i < (N/3) -1:
            palabra =  str (func_datos ("Ingrese una palabra : ", validar_palabra))
            palabra = palabra.lower()
            if palabra == "fin":
                break
            i= i+1
            diccionario.append (palabra)
        print (diccionario)

        def validar_archivo(nombre):   
            return int (len (nombre) < 30) 

        nombre_archivo = str (func_datos ("Ingrese el nombre del archivo (menor a 30 caracteres): ", validar_archivo))
        crear_archivo = open (nombre_archivo, "w")
        print ("El archivo se guardó correctamente")
        return N, diccionario, nombre_archivo
        

class Escritor:
    def __init__(self,tablero,diccionario,nombre_archivo):    
        self.tablero = tablero
        self.diccionario = diccionario
        self.nombre_archivo = nombre_archivo
    


    def escribir_tablero (self): 
        with open (self.nombre_archivo + ".csv", "w",newline= "") as armadoDeTablero:
            escritor = csv.writer (armadoDeTablero)
            escritor.writerows (self.tablero)
            print ("Se creó la matriz correctamente")
        
    def escribir_solucion(self):
        with open (self.nombre_archivo + "_solucion.csv", "w", newline= "") as armadoTablero:
            titulos=["palabra","x_inicio", "y_inicio","x_final","y_final"]
            writer = csv.DictWriter(armadoTablero, fieldnames=titulos )
            writer.writeheader()
            for clave,valor in (self.diccionario).items():
                dicci = {"palabra": clave}
                dicci.update(valor)
                writer.writerow (dicci)
            print ("Se guardaron las palabras ingresadas")
    
        

class Programa:
    def main():
        N, diccionario, nombre_archivo = Obtener_datos().obtener_datos_usuario() 
        diccionario, tablero =  Generar_tablero(N, diccionario, "tablero").generar(diccionario)
        prueba_escritor = Escritor (tablero,diccionario,nombre_archivo)
        prueba_escritor.escribir_tablero ()
        prueba_escritor.escribir_solucion()
        
Programa.main ()