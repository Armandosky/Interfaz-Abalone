import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from scipy import stats
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error



def histograma(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    plot.hist(x=pepito[dato], density='true', rwidth=(0.9))
    plot.title("Histograma")
    plot.xlabel(dato)
    plot.ylabel("Frecuencia")

def histograma_Atipicos(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    for x in [str(dato)]:
        q75,q25 = np.percentile(pepito.loc[:,x],[75,25])
        intr_qr = q75-q25
        max = q75+(float(alfa.get())*intr_qr)
        min = q25-(float(alfa.get())*intr_qr)
        pepito.loc[pepito[x] < min,x] = np.nan
        pepito.loc[pepito[x] > max,x] = np.nan   
    pepito = pepito.dropna(axis = 0) 
    plot.hist(x=pepito[dato], density='true', rwidth=(0.9))
    plot.title("Histograma")
    plot.xlabel(dato)
    plot.ylabel("Frecuencia")

def cajas_bigotes(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    plot.boxplot(pepito[dato])
    plot.title("Caja y bigotes")
    plot.xlabel(dato)

def cajas_bigotes_atipicos(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    for x in [str(dato)]:
        q75,q25 = np.percentile(pepito.loc[:,x],[75,25])
        intr_qr = q75-q25
        max = q75+(float(alfa.get())*intr_qr)
        min = q25-(float(alfa.get())*intr_qr)
        pepito.loc[pepito[x] < min,x] = np.nan
        pepito.loc[pepito[x] > max,x] = np.nan  
    pepito = pepito.dropna(axis = 0) 
    plot.boxplot(pepito[dato])
    plot.title("Caja y bigotes")
    plot.xlabel(dato)
    
def probabilidad_normal(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    stats.probplot(pepito[dato], dist=stats.norm, sparams=(6,), plot=plot)
    plot.title(dato)
    plot.xlabel("Cuantiles tericos")
    plot.ylabel("valores ordenados")
    
def probabilidad_normal_atipicos(dato):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    for x in [str(dato)]:
        q75,q25 = np.percentile(pepito.loc[:,x],[75,25])
        intr_qr = q75-q25
        max = q75+(float(alfa.get())*intr_qr)
        min = q25-(float(alfa.get())*intr_qr)
        pepito.loc[pepito[x] < min,x] = np.nan
        pepito.loc[pepito[x] > max,x] = np.nan  
    pepito = pepito.dropna(axis = 0) 
    stats.probplot(pepito[dato], dist=stats.norm, sparams=(6,), plot=plot)
    plot.title(dato)
    plot.xlabel("Cuantiles tericos")
    plot.ylabel("valores ordenados")
    
def dispersion(dato1, dato2):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    plot.scatter((pepito[dato1]),(pepito[dato2]))
    plot.title("Dispersion")
    plot.xlabel(dato1)
    plot.ylabel(dato2)
    
def dispersion_atipicos(dato1, dato2):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    for x in [str(dato1)]:
        q75,q25 = np.percentile(pepito.loc[:,x],[75,25])
        intr_qr = q75-q25
        max = q75+(float(alfa.get())*intr_qr)
        min = q25-(float(alfa.get())*intr_qr)
        pepito.loc[pepito[x] < min,x] = np.nan
        pepito.loc[pepito[x] > max,x] = np.nan  
    for x in [str(dato2)]:
        q75,q25 = np.percentile(pepito.loc[:,x],[75,25])
        intr_qr = q75-q25
        max = q75+(float(alfa.get())*intr_qr)
        min = q25-(float(alfa.get())*intr_qr)
        pepito.loc[pepito[x] < min,x] = np.nan
        pepito.loc[pepito[x] > max,x] = np.nan 
    pepito = pepito.dropna(axis = 0) 
    plot.scatter((pepito[dato1]),(pepito[dato2]))
    plot.title("Dispersion")
    plot.xlabel(dato1)
    plot.ylabel(dato2)

def modelounoauno(tamañoentrenamiento,X,Y):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        Y,
                                        train_size   = 0.8,
                                    )
    modelo = LinearRegression()
    modelo.fit(X = np.array(X_train).reshape(-1, 1), y = y_train)
    datosobtenidos = modelo.predict(X = np.array(X_test).reshape(-1,1))
    return datosobtenidos
    
#modelo uno a muchos
#x es una lista
def modelounoamuchos(tamañoentrenamiento,X,Y):
    archivo='abalone.csv'
    pepito = pd.read_csv(archivo)
    pepito.columns=["Sex","Length","Diameter","Height","Whole weight","Shucked weight","Viscera weight","Shell weight","Rings"]
    X = X.drop(['sex'], axis=1)
    Y = Y[0:len(X)]
    X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        Y,
                                        train_size   = 0.8,
                                    )
    modelo = LinearRegression()
    modelo.fit(X = np.array(X_train), y = y_train)
    datosobtenidos = modelo.predict(X = np.array(X_test))
    return datosobtenidos


def opcionCheck():
    if Longitud.get()==1 and not "Length" in textoFinal:
        textoFinal.append("Length")
    if Diametro.get()==1 and not "Diameter" in textoFinal:
        textoFinal.append("Diameter")
    if Altura.get()==1 and not "Height" in textoFinal:
        textoFinal.append("Height")
    if Pesoentero.get()==1 and not "Whole weight" in textoFinal:
        textoFinal.append("Whole weight")
    if Pesodescascarillado.get()==1 and not "Shucked weight" in textoFinal:
        textoFinal.append("Shucked weight")
    if Pesodelasvisceras.get()==1 and not "Viscera weight" in textoFinal:
        textoFinal.append("Viscera weight")
    if Pesodelacarcasa.get()==1 and not "Shell weight" in textoFinal:
        textoFinal.append("Shell weight")
    if Anillos.get()==1 and not "Rings" in textoFinal:
        textoFinal.append("Rings")

def graficaNormal():
    if(len(textoFinal)==1):
        if(varOpcion.get()==1):
            fig = plot.figure()
            fig.add_subplot(111)
            histograma(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
        elif(varOpcion.get()==2):
            fig = plot.figure()
            fig.add_subplot(111)
            cajas_bigotes(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
        elif(varOpcion.get()==3):
            fig = plot.figure()
            fig.add_subplot(111)
            probabilidad_normal(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
    elif(len(textoFinal)==2):
        if(varOpcion.get()==4):
            fig = plot.figure()
            fig.add_subplot(111)
            dispersion(textoFinal[0], textoFinal[1])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
    else:
        messagebox.showinfo(message="Selección incorrecta", title="Error")

def graficaAtipicos():
    if(len(textoFinal)==1):
        if(varOpcion.get()==1):
            fig = plot.figure()
            fig.add_subplot(111)
            histograma_Atipicos(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
            plot.subplots()
        elif(varOpcion.get()==2):
            fig = plot.figure()
            fig.add_subplot(111)
            cajas_bigotes_atipicos(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
            plot.subplots()
        elif(varOpcion.get()==3):
            fig = plot.figure()
            fig.add_subplot(111)
            probabilidad_normal_atipicos(textoFinal[0])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
            plot.subplots()
    elif(len(textoFinal)==2):
        if(varOpcion.get()==4):
            fig = plot.figure()
            fig.add_subplot(111)
            dispersion_atipicos(textoFinal[0], textoFinal[1])
            canvas = FigureCanvasTkAgg(fig, master=root) 
            canvas.draw()
            canvas.get_tk_widget().place(x=500,y=50)
            plot.subplots()

    else:
        messagebox.showinfo(message="Selección incorrecta", title="Error")
    
def cerrar():   
    root.quit()     
    root.destroy()
    
    
root=tk.Tk()
root.geometry("1000x530") 
root.title("Interfaz de abalones")

Label1 = tk.Label(root, text="Tipo de grafico").place(x=50, y=50)
Label2 = tk.Label(root, text="Tipo de Dato").place(x=50, y=250)
Label3 = tk.Label(root, text="Factor alfa de los atipicos").place(x=50, y=400)

alfa =tk.StringVar()
entry1 = tk.Entry(root, textvariable=alfa).place(x=300, y=400)



varOpcion = tk.IntVar()
button1 =tk.Radiobutton(root, text="Histograma", variable=varOpcion, value=1).place(x=300,y=20)
button2 =tk.Radiobutton(root, text="Cajas y bigotes", variable=varOpcion, value=2).place(x=300,y=40)
button3 =tk.Radiobutton(root, text="probabilidad normal", variable=varOpcion, value=3).place(x=300,y=60)
button4 =tk.Radiobutton(root, text="Dispersion", variable=varOpcion, value=4).place(x=300,y=80)
button5 =tk.Radiobutton(root, text="Regresión Lineal", variable=varOpcion, value=5).place(x=300,y=100)
    
Longitud=tk.IntVar()
Diametro=tk.IntVar()
Altura=tk.IntVar()
Pesoentero=tk.IntVar()
Pesodescascarillado=tk.IntVar()
Pesodelasvisceras=tk.IntVar()
Pesodelacarcasa=tk.IntVar()
Anillos=tk.IntVar()

textoFinal =[]


       

boton1 = tk.Checkbutton(root, text="Longitud", variable=Longitud, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=150)
boton2 = tk.Checkbutton(root, text="Diametro", variable=Diametro, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=170)
boton3 = tk.Checkbutton(root, text="Altura", variable=Altura, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=190)
boton4 = tk.Checkbutton(root, text="Peso entero", variable=Pesoentero, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=210)
boton5 = tk.Checkbutton(root, text="Peso descascarillado", variable=Pesodescascarillado, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=230)
boton6 = tk.Checkbutton(root, text="Peso de las visceras", variable=Pesodelasvisceras, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=250)
boton7 = tk.Checkbutton(root, text="Peso de la carcasa", variable=Pesodelacarcasa, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=270)
boton8 = tk.Checkbutton(root, text="Anillos", variable=Anillos, onvalue=1, offvalue=0, command=opcionCheck).place(x=300,y=290) 
         
botonGraficar1 = tk.Button(root, text="Graficar", command=graficaNormal).place(x=190,y=360)
botonGraficar2 = tk.Button(root, text="Graficar sin atípicos", command=graficaAtipicos).place(x=150,y=450)

    
buttonCerrar = tk.Button(root, text="Cerrar interfaz", command=cerrar).place(x=700,y=350)

root.mainloop()






