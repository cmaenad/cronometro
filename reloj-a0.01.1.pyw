# -*- coding: utf-8 -*-
"""

Descripcion: Programa de tiempo que busca dar de una forma más eficiente y 
practica información al usuario sobre el tiempo que lleva haciendo una actividad

caracteristicas
-Cronometro 24h
-Boton de pausa
-Boton de reinicio del cronometro
-Ventana semitransparente al quitar como ventana principal
*Precision de tiempo

Fecha de creacion: 21 de noviembre de 2021 
Última modificación: 3 de diciembre de 2021
"""
from tkinter import *
#esto de abajo para poder poner el icono en la barra de tareas (copiado de stack overflow)
import ctypes
myappid = 'eacm.reloj.contador.a0.01'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#base64 para que, en base al texto de abajo, podamos escribir el icono en tiempo de ejecucion en un
#archivo y asi poder guardar todo el script como un solo ejecutable y ya
import base64
import os
##The Base64 icon version as a string
icon = \
"""AAABAAEAZGQQAAEABAD4GgAAFgAAACgAAABkAAAAyAAAAAEABAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAA////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAERERERER
EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEREREREREREREREAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERERERAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREREREQAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERERERERERERERERERERERAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREREREREREREAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAABEREREREREREREREREREREREREREREAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAABEREREREREREREREREREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAEREREREREREREREREREREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERER
EREREREREREREREREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERERERERER
ERERERERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERERERER
ERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAERERERERERERERERERERERERERER
ERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERERERERERERERERERERERERERERERER
ERERERAAAAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERERERERERERERERERERERERERERER
AAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREREREREREREREREREREREREREQAAAAAA
AAAAAAAAAAAAAAAAAAABEREREREREREREREREREREREREREREREREREREREREREQAAAAAAAAAAAA
AAAAAAAAAAAAEREREREREREREREREREREREREREREREREREREREREREREQAAAAAAAAAAAAAAAAAA
AAAAAREREREREREREREREREREREREREREREREREREQABEREREREQAAAAAAAAAAAAAAAAAAAAAAER
ERERERERERERERERERERERERERERERERERAAABEREREREAAAAAAAAAAAAAAAAAAAAAARERERERER
EREREREREREREREREREREREREREAAAAREREREREAAAAAAAAAAAAAAAAAAAABERERERERERERERER
EREREREREREREREREREQAAAAEREREREREAAAAAAAAAAAAAAAAAAAARERERERERERERERERERERER
ERERERERERERAAAAARERERERERAAAAAAAAAAAAAAAAAAABERERERERERERERERERERERERERERER
EREREAAAABERERERERERAAAAAAAAAAAAAAAAAAAREREREREREREREREREREREREREREREREREQAA
AAEREREREREREQAAAAAAAAAAAAAAAAABERERERERERERERERERERERERERERERERERAAAAARERER
EREREREQAAAAAAAAAAAAAAAAAREREREREREREREREREREREREREREREREREAAAABERERERERERER
EAAAAAAAAAAAAAAAAAEREREREREREREREREREREREREREREREREQAAAAERERERERERERERAAAAAA
AAAAAAAAAAARERERERERERERERERERERERERERERERERAAAAARERERERERERERERAAAAAAAAAAAA
AAAAEREREREREREREREREREREREREREREREREAAAABEREREREREREREREQAAAAAAAAAAAAAAABER
EREREREREREREREREREREREREREREQAAAAEREREREREREREREREAAAAAAAAAAAAAAAERERERERER
ERERERERERERERERERERERAAAAAREREREREREREREREREAAAAAAAAAAAAAABERERERERERERERER
EREREREREREREREAAAABERERERERERERERERERAAAAAAAAAAAAAAARERERERERERERERERERERER
EREREREQAAAAEREREREREREREREREREQAAAAAAAAAAAAAAERERERERERERERERERERERERERERER
AAAAAREREREREREREREREREREAAAAAAAAAAAAAABEREREREREREREREREREREREREREREAAAABER
EREREREREREREREREREAAAAAAAAAAAAAEREREREREREREREREREREREREREREQAAAAERERERERER
ERERERERERERAAAAAAAAAAAAABERERERERERERERERERERERERERERAAAAARERERERERERERERER
EREREQAAAAAAAAAAAAAREREREREREREREREREREREREREREAAAABEREREREREREREREREREREREA
AAAAAAAAAAAAEREREREREREREREREREREREREREQAAAAERERERERERERERERERERERERAAAAAAAA
AAAAABERERERERERERERERERERERERERAAAAAREREREREREREREREREREREREQAAAAAAAAAAAAAR
EREREREREREREREREREREREREQAAABEREREREREREREREREREREREREAAAAAAAAAAAAAERERERER
ERERERERERERERERERAAAAERERERERERERERERERERERERERAAAAAAAAAAAAABERERERERERERER
EREREREREREQAAAREREREREREREREREREREREREREQAAAAAAAAAAAAARERERERERERERERERERER
EREREAAAEREREREREREREREREREREREREREAAAAAAAAAAAAAERERERERERERERERERERERERERAA
ABERERERERERERERERERERERERERAAAAAAAAAAAAABEREREREREREREREREREREREREQAAARERER
EREREREREREREREREREREQAAAAAAAAAAAAAREREREREREREREREREREREREREAAAERERERERERER
EREREREREREREREAAAAAAAAAAAAAARERERERERERERERERERERERERAAABERERERERERERERERER
EREREREQAAAAAAAAAAAAAAEREREREREREREREREREREREREQAAARERERERERERERERERERERERER
EAAAAAAAAAAAAAABEREREREREREREREREREREREREAAAERERERERERERERERERERERERERAAAAAA
AAAAAAAAARERERERERERERERERERERERERAAABEREREREREREREREREREREREREQAAAAAAAAAAAA
AAEREREREREREREREREREREREREQAAAREREREREREREREREREREREREREAAAAAAAAAAAAAAAERER
EREREREREREREREREREREAAAEREREREREREREREREREREREREQAAAAAAAAAAAAAAABERERERERER
ERERERERERERERAAABEREREREREREREREREREREREREAAAAAAAAAAAAAAAARERERERERERERERER
EREREREQAAARERERERERERERERERERERERERAAAAAAAAAAAAAAAAARERERERERERERERERERERER
EAAAEREREREREREREREREREREREREAAAAAAAAAAAAAAAAAERERERERERERERERERERERERAAABER
ERERERERERERERERERERERAAAAAAAAAAAAAAAAABEREREREREREREREREREREREQAAARERERERER
EREREREREREREREQAAAAAAAAAAAAAAAAABEREREREREREREREREREREREAAAERERERERERERERER
ERERERERAAAAAAAAAAAAAAAAAAARERERERERERERERERERERERAAABERERERERERERERERERERER
EQAAAAAAAAAAAAAAAAAAAREREREREREREREREREREREQAAARERERERERERERERERERERERAAAAAA
AAAAAAAAAAAAAAEREREREREREREREREREREREAAAEREREREREREREREREREREREQAAAAAAAAAAAA
AAAAAAAAERERERERERERERERERERERAAABERERERERERERERERERERERAAAAAAAAAAAAAAAAAAAA
AAEREREREREREREREREREREQAAAREREREREREREREREREREREAAAAAAAAAAAAAAAAAAAAAABERER
EREREREREREREREREAAAERERERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAABERERERERER
ERERERERERAAABEREREREREREREREREREREAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERER
EREQAAAREREREREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAABEREREREREREREREREREAAA
ERERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERERERAAABERERER
EREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREQAAARERERERERERER
ERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREAAAEREREREREREREREREREA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERERERERERERERAAABEREREREREREREREREQAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAABEREREREREREREREQAAARERERERERERERERERAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAABEREREREREREREREAAAERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAABERERERERERERERAAABEREREREREREREREAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAABERERERERERERERAAEREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
EREREREREREREREREREREREREREREQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAERERER
ERERERERERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARERERERERER
ERERERERERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABERERERERERERERER
ERERERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREREREREREREQAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEREREREREREREREAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAREREREREAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP/////AAAAAP/////AAAAD////+AAAAAAf////wAAAA
////+AAAAAAB////8AAAAP///+AAAAAAAH////AAAAD///+AAAAAAAAf///wAAAA///+AAAAAAAA
B///8AAAAP//+AAAAAAAAAH///AAAAD///AAAAAAAAAA///wAAAA///gAAAAAAAAAH//8AAAAP//
wAAAAAAAAAA///AAAAD//4AAAAAAAAAAD//wAAAA//4AAAAAAAAAAAf/8AAAAP/8AAAAAAAAAAAD
//AAAAD/+AAAAAAAAAAAAf/wAAAA//AAAAAAAAAAAAD/8AAAAP/gAAAAAAAAAAAAf/AAAAD/4AAA
AAAAAAAAAD/wAAAA/8AAAAAAAAAAAAA/8AAAAP+AAAAAAAAAAAAAH/AAAAD/AAAAAAAAAAAAAA/w
AAAA/gAAAAAAAAAAAAAH8AAAAP4AAAAAAAAAAAAAA/AAAAD8AAAAAAAAAAAAAAPwAAAA+AAAAAAA
AAAAAAAB8AAAAPgAAAAAAAAAAAAAAfAAAADwAAAAAAAAAAAAAADwAAAA8AAAAAAAAAAAAAAA8AAA
AOAAAAAAAAAAAAAAAHAAAADgAAAAAAAAAAAAAABwAAAAwAAAAAAAAAAAAAAAMAAAAMAAAAAAAAAA
AAAAADAAAACAAAAAAAAAAAAAAAAQAAAAgAAAAAAAAAAAAAAAEAAAAIAAAAAAAAAAAAAAABAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAA
AAAAAAAAAAAAABAAAACAAAAAAAAAAAAAAAAQAAAAwAAAAAAAAAAAAAAAEAAAAMAAAAAAAAAAAAAA
ADAAAADAAAAAAAAAAAAAAAAwAAAA4AAAAAAAAAAAAAAAcAAAAOAAAAAAAAAAAAAAAHAAAADwAAAA
AAAAAAAAAADwAAAA8AAAAAAAAAAAAAAA8AAAAPgAAAAAAAAAAAAAAfAAAAD4AAAAAAAAAAAAAAHw
AAAA/AAAAAAAAAAAAAAD8AAAAP4AAAAAAAAAAAAAA/AAAAD+AAAAAAAAAAAAAAfwAAAA/wAAAAAA
AAAAAAAP8AAAAP+AAAAAAAAAAAAAH/AAAAD/wAAAAAAAAAAAAD/wAAAA/+AAAAAAAAAAAAB/8AAA
AP/gAAAAAAAAAAAAf/AAAAD/8AAAAAAAAAAAAP/wAAAA//gAAAAAAAAAAAH/8AAAAP/8AAAAAAAA
AAAD//AAAAD//gAAAAAAAAAAB//wAAAA//+AAAAAAAAAAB//8AAAAP//wAAAAAAAAAA///AAAAD/
/+AAAAAAAAAAf//wAAAA///wAAAAAAAAAP//8AAAAP///AAAAAAAAAP///AAAAD///4AAAAAAAAH
///wAAAA////gAAAAAAAH///8AAAAP///+AAAAAAAH////AAAAD////4AAAAAAH////wAAAA////
/wAAAAAH////8AAAAP/////AAAAAP/////AAAAA="""
icondata= base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()

#threading para hacer el proceso de "subrutina" o "interrupcion" para que
#despues de 1 segundo, se sume uno al contador
import threading

#clase contador, el constructor incluye una variable global para guardar si el reloj esta pausado
#y variables por cada medida a mostrar en el reloj
class contador:
    def __init__(self):
        global pausa
        self.segundos=0
        self.minutos=0
        self.horas=0
        pausa=False
    #metodo para poner en estado original el constructor, pero dejandolo pausado
    def reiniciar(self):
        global pausa
        self.segundos=0
        self.minutos=0
        self.horas=0
        pausa=True
    #metodo para solo poner pausa o quitar la pausa 
    def pausar(self):
        global pausa
        if pausa==False:
            pausa=True
        else:
            pausa=False
    #metodo de "interrupcion" para que despues de 1 segundo, se llame al mismo metodo una y otra vez
    #sumando 1 a la variable segundo, y como un reloj, cambiar los minutos y horas acorde a eso
    def aumenta(self):
        self.cuenta=threading.Timer(1.0, self.aumenta)
        self.cuenta.start()
        global pausa
        if pausa is True:
            return
        else:
            self.segundos+=1
            if(self.segundos>=60):
                self.segundos=0
                self.minutos+=1
                if(self.minutos>=60):
                    self.minutos=0
                    self.horas+=1
                    if(self.horas>=24):
                        self.horas=0
    #metodo para convertir un entero de 1 o 2 cifras y devolver version de cadena
    def hazcadena(self,valor):
        if(valor<10):
            cadena="0"+str(valor)
        else:
            cadena=str(valor)
        return cadena
    
    #metodo que llama al anterior por cada medida de tiempo y lo junta en una sola cadena que devuelve
    def conviertehoras(self):
        cadena=self.hazcadena(self.horas)+":"
        cadena+=self.hazcadena(self.minutos)+":"
        cadena+=self.hazcadena(self.segundos)
        return cadena
    
#clase de la GUI, (segun entiendo en python los parametros se pasan por referencia siempre, entonces se esta cambiando
#a ventana, que es de tipo tkinter.Tk()
#recibe a ventana y reloj, pues reloj se creo antes para iniciar algunas variables (no se si se pueda optimizar) 
class VentanaPrincipal:
    #constructor que define 3 variables globales, la etiqueta label1 del texto del reloj, el boton para parar y el texto que cambia
    #al ponerse pausa o no
    def __init__(self,ventana,reloj):
        global label1
        global botonParar
        global textitodetener
        
        #nombre de la ventana y definiccion del texto de la etiqueta del reloj, con fuente y posicion
        ventana.title("Contador")
        label1=Label(ventana,text=reloj.conviertehoras())
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=1)
        
        #boton de pausa, que detiene el reloj al pulsarse
        botonParar = Button (ventana, text = textitodetener, command = reloj.pausar)
        botonParar.grid(row=2)
        botonParar.configure(width=10)
        
        #boton para borrar el reloj y pararlo
        botonReinicia = Button (ventana, text = "Reiniciar", command = reloj.reiniciar)
        botonReinicia.grid(row=3)
        botonReinicia.configure(width=10)
        
        
            
#funcion del programa (no de ninguna clase), que cambia el texto de las etiquetas de la ventanita y del boton
def cambiaetiqueta():
    
    global label1
    global afterid
    global botonParar
    global pausa
    #configura el texto de la etiqueta de reloj cada vez que entra a esta funcion el programa
    label1.config(text=reloj.conviertehoras())
    
    #cambia el texto del boton si esta en pausa o si no
    if pausa is True:
        textitodetener="Iniciar"
    else:
        textitodetener="Pausar"
    botonParar.config(text=textitodetener)
    
    #cambia la transparencia de la ventana si esta en primer plano o no (util con el hotkey de always on top)
    if ventana.focus_displayof():
            ventana.attributes("-alpha",1.0)
    else:
        ventana.attributes("-alpha",0.4)
    
    #try except para que no salgan errores raros, lo de dentro hace que se llame a esta funcion cada 100 ms
    try:
        afterid=ventana.after(100,cambiaetiqueta)
    except:
        pass

#funcion para cuando se cierra el programa, cancela el llamar a cambia etiqueta y borra el thread del tiempo
#despues destruye el objeto ventana
def alcerrar():
    global afterid
    ventana.after_cancel(afterid)
    ventana.destroy()

#se hace un objeto "ventana" de tkinter
ventana=Tk()

#cuando se cierra la ventana, llama a alcerrar()
ventana.protocol("WM_CLOSE_WINDOW",alcerrar)

#se definen las variables globales del programa, se inicializa textitodetener para mostrar pausar, y se declara que el
#reloj esta iniciado
global label1
global pausa
global textitodetener
textitodetener="Pausar"
pausa=False

#se crea el objeto reloj de tipo contador y se inicia el thread (la "interrupcion") para aumentar la cuenta
reloj=contador()
reloj.aumenta()

VentanaPrincipal(ventana,reloj)

#el archivo temporal del icono se define para ventana y despues se borra
ventana.iconbitmap(tempFile)
os.remove(tempFile)

#se llama a cambiaetiqueta para que empiece a actualizar las etiquetas
cambiaetiqueta()

#loop de ventana
ventana.mainloop()