import pandas as pd
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(True)

class Graphs():
    def __init__(self):
        pass

    def graphSelected(self, filter, GRAPHS, df):
        if filter.get() == GRAPHS[0]:
            self.firstGraph(GRAPHS, df)
    
        elif filter.get() == GRAPHS[1]:
            self.secondGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[2]:
            self.thirdGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[3]:
            self.fourthGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[4]:
            self.fifthGraph(GRAPHS, df)
        
        elif filter.get() == GRAPHS[5]:
            self.sixthGraph(GRAPHS, df)
        
    def firstGraph(self, GRAPHS, df):
        newDf = dict(df.groupby('País')['Cliente'].size())
        plt.bar(newDf.keys(), newDf.values())
        plt.title(GRAPHS[0])
        plt.xlabel("Paises")
        plt.ylabel("Cantidad de clientes")
        plt.show()

    def secondGraph(self, GRAPHS, df):
        newDf = dict(df.groupby('Fecha')['Cliente'].size())
        plt.bar(newDf.keys(), newDf.values())
        plt.title(GRAPHS[1])
        plt.xlabel("Fechas")
        plt.ylabel("Clientes")
        plt.show()

    def thirdGraph(self, GRAPHS, df):
        newDf = dict(df.groupby('Venta')['Cliente'].size())
        plt.bar((df['Cliente']), (newDf.keys()))
        plt.title(GRAPHS[2])
        plt.xlabel("Clientes")
        plt.ylabel("Ventas")
        plt.show()

    def fourthGraph(self, GRAPHS, df):
        newDf = dict(df.groupby('CostoEnvío')['Cliente'].size())
        plt.bar((df['Cliente']), (newDf.keys()))
        plt.title(GRAPHS[3])
        plt.xlabel("Clientes")
        plt.ylabel("Costo de envío")
        plt.show()

    def fifthGraph(self, GRAPHS, df):
        plt.bar(df['País'], df['TotalVenta'])
        plt.title(GRAPHS[4])
        plt.xlabel("Países")
        plt.ylabel("Ventas totales")
        plt.show()

    def sixthGraph(self, GRAPHS, df):
        plt.bar(df['Cliente'], df['TotalVenta'])
        plt.title(GRAPHS[5])
        plt.xlabel("Clientes")
        plt.ylabel("Ventas totales")
        plt.show()
    
    def saveGraph(self, filter, GRAPHS):
        for graph in GRAPHS:
            if filter.get() == graph:
                graphName = graph+'.png'
                imageName = graphName.replace(' ','_') 
                plt.savefig(imageName)

if __name__ == '__main__':

    df = pd.read_csv("data.txt")

    graphsObject = Graphs()

    GRAPHS = ('Clientes por país', 'Clientes por fecha', 'Ventas de cada cliente', 'Costo de envío por cliente', 'Ventas totales por país', 'Ventas totales por cliente')

    mw = tk.Tk()
    mw.title('Gráficas')
    mw.geometry("600x300") 
    mw.resizable(0, 0)

    selectGraph = ttk.Combobox(mw,value=GRAPHS)
    selectGraph.set('Seleccione una gráfica')
    selectGraph.place(x = 210, y = 15, width=210, height=35)

    btnGraph = tk.Button(text='Obtener gráfica', command= lambda: graphsObject.graphSelected(selectGraph, GRAPHS, df))
    btnGraph.place(x = 250, y = 80, width=130, height=35)

    saveInstructions = Label(text = "Abra la gráfica para descargarla").place(x = 203,y = 140) 

    btnSaveGraphs = tk.Button(text='Descargar gráfica', command=lambda: graphsObject.saveGraph(selectGraph, GRAPHS))
    btnSaveGraphs.place(x = 250, y = 170, width=130, height=35)

    mw.mainloop()