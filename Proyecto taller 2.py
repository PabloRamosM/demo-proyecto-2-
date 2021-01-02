from tkinter import *
import os
from threading import Thread
import threading
import time
import random
from random import shuffle 
from pygame import mixer
from PIL import ImageTk, Image
#Funcion que carga las imagenes, se le da la ruta actual. 
def cImagen(archivo):   
    ruta =os.path.join("Img",archivo)
    imagen=PhotoImage(file=ruta)
    return imagen
#Ventana y canvas principal
ventana=Tk()
ventana.title('Pantalla de incio')
ventana.minsize(1000,700)
ventana.resizable(width=NO, height=NO)

C_principal=Canvas(ventana,width=1000,height=700, bg='white')
C_principal.place(x=0,y=0)



#Wallpaper y el logo del juego 
C_principal.fondo=cImagen("wallpaper.png")
imgcanvas=C_principal.create_image(0,0,anchor=NW,image=C_principal.fondo)
logo=cImagen("logo2.png")
logo1=C_principal.create_image(410,5,anchor=NW,image=logo)

def about():
    global top2
    top2=Toplevel()
    top2.title('Ventana de Créditos')
    top2.minsize(1000,700)
    top2.resizable(width=NO, height=NO)
    Canvas_creditos=Canvas(top2,width=1000,height=700, bg='white')
    Canvas_creditos.place(x=0,y=0)
    Canvas_creditos.image2=cImagen("wallpaper.png")
    imgcanvas2=Canvas_creditos.create_image(0,0,anchor=NW,image=Canvas_creditos.image2)
    boto2=Button(top2,text='volver a menu',command=close_creditos)
    boto2.place(x=500,y=620)
    ventana.withdraw() 

def close_creditos():
    ventana.deiconify()
    top2.destroy()


















btn_entry=Button(C_principal,text='Play',bg='blue',fg='white',height=2,width=15,font=("Arial bold",10))
btn_entry.place(x=500,y=200)

btn_entry=Button(C_principal,text='Options',bg='blue',fg='white',height=2,width=15,font=("Arial bold",10))
btn_entry.place(x=500,y=300)

btn_entry=Button(C_principal,text='High Scores',bg='blue',fg='white',height=2,width=15,font=("Arial bold",10))
btn_entry.place(x=500,y=400)

btn_entry=Button(C_principal,text='About',bg='blue',fg='white',height=2,width=15,font=("Arial bold",10),command=about)
btn_entry.place(x=500,y=500)





ventana.mainloop()
