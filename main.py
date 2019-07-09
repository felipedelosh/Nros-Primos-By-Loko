"""
7/8/2019

felipedelosh

rellenar un vector con los n primos
interfaz grafica tkinter

instrucciones:

1 - ingrese un numero [1, 1000] en el entry
2 - presione el btn START
3 - si el nro es mayor de 12 utilize los btns >> y << para moverse adelante y atraz

"""
from tkinter import *


class Software:
    def __init__(self):
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, width=720, height=300, bg="snow")
        self.lblIngreseTamanoVector = Label(self.tela, text="Ingrese el tamano del vector: ")
        self.txtTamano = Entry(self.tela)
        self.btnPLAY = Button(self.tela, text="START", bg="orange", command=self.calcularPrimos)
        self.btnSig = Button(self.tela, text=">>", bg="green", command=lambda : self.actualizarListaPrimos(12))
        self.btnAnt = Button(self.tela, text="<<", bg="green", command=lambda : self.actualizarListaPrimos(-12))
        """Variables"""
        self.tamanoVector = 0
        self.vectorPrimos = []
        self.punteroPrimo = 0 # Este solo apunta a una posicion del vector
        # Estas son las variables para hacer scroll en el vector
        self.listoParaPintar = False
        self.posPintar = 0
        self.posNumerosCinta = []
        self.visualizarInterfaz()


    """"Este metodo pinta la interfaz"""
    def visualizarInterfaz(self):
        self.pantalla.title("Nprimos by loko")
        self.pantalla.geometry("720x300")
        self.tela.place(x=0, y=0)
        self.lblIngreseTamanoVector.place(x=10, y=20)
        self.txtTamano.place(x=200, y=20)
        self.btnPLAY.place(x=650, y=20)
        self.pantalla.mainloop()

    """Los botones anterior y siguiente solo se muestran si hay scroll"""
    def pintarBtnNext(self):
        self.btnSig.place(x=680, y=150)

    def pintarBtnPrevius(self):
        self.btnAnt.place(x=10, y=150)


    """Los botones anterior y siguiente se borran dependiendo si no hay que mostrar"""
    def borrarBTNNext(self):
        self.btnSig.place_forget()

    def borrarBTNPrevius(self):
         self.btnAnt.place_forget()


    """Este metodo procede a calcular los primos"""
    def calcularPrimos(self):
        try:
            # Se reinician las variables
            self.punteroPrimo = 0
            self.posPintar = 0
            self.listoParaPintar = False
            self.posNumerosCinta = []
            self.tela.delete("numeritos")
            self.tela.delete("leyenda")
            n = int(self.txtTamano.get())
            if n <= 1000:
                # Se procede a rellenar el vector con -1 >> solo para el inicio
                self.tamanoVector = n # Para rellenar el vector
                self.inizializarVectorPrimos() # Se rellena el vector en vacio
                # Se procede a llenar el vector de primos
                self.rellenarVectorPrimos()
                # Se procede a pintar el vector de primos y los primos
                self.pintarCintaDePrimos()
                # Si el vector es muy grande se pintan >> y <<
                if n > 12:
                    self.pintarBtnNext()
                else:
                    self.borrarBTNNext()
                    self.borrarBTNPrevius()

        except:
            self.ventanaEmergente("Error", "Ingrese un numero entre 1 y 1000")
    
    """Parecido al joptionpane de java"""
    """Aqui se puede mostrar cualquier mensaje en ena ventana emergente"""
    def ventanaEmergente(self, titulo, mensaje):
        top = Toplevel()
        top.title(titulo)
        msg = Message(top, text=str(mensaje))
        msg.pack()
        button = Button(top, text="ACEPTAR", command=top.destroy)
        button.pack()

    
    """
    Existe un vector: self.vectorPrimos aka se reinicia y se pone todo en -1
    """
    def inizializarVectorPrimos(self):
        self.vectorPrimos = []
        for i in range(self.tamanoVector):
            self.vectorPrimos.append(-1)

    """Este metodo calcula los primos 1 a 1
    1 - se procede a escogerlos iterativamente... primero viene el 1 si es primo se agrega
    luego viene el 2 si es primo se agrega, luego viene el 3 si es primo se agrega...
    """
    def rellenarVectorPrimos(self):
        candidato = 2
        while self.punteroPrimo < self.tamanoVector:
            # Se procede a calcular la pos del puntero para el primo ?
            if self.esPrimo(candidato):
                # El numero es primo... se agrega luego aumenta el puntero
                self.vectorPrimos[self.punteroPrimo] = candidato
                self.punteroPrimo = self.punteroPrimo + 1
            
            candidato = candidato + 1

        self.listoParaPintar = True

    
    """Este metodo me dice si un numero es primo o no"""
    def esPrimo(self, x):
        """Recordad que el 1 no es primo
        un primo es aquel que puede ser dividido por el mismo y la unidad
        """
        divisor = 0
        for i in range(2, x+1):
            if x%i == 0:
                divisor = divisor + 1
                if divisor > 1:
                    return False
        return True 


    """Este metodo visualiza la cinta de primos"""
    def pintarCintaDePrimos(self):
        # Se pinta la cinta con cuadritos
        for i in range(0, 12):
            self.tela.create_rectangle((51*(i+1)), 150, (51*(i+2)), 180, width=5, fill='red')
            # Se guardan x0 y y0 de la cinta:
            self.posNumerosCinta.append((51*(i+1)))

        # Se proceden a pintar los numeritos que existan

        if len(self.vectorPrimos) < 12:
            # Se pinta solo lo que quepa
            aux = 0
            for i in range(len(self.vectorPrimos)):
                self.tela.create_text(self.posNumerosCinta[aux]+20,
                 165,
                  text=str(self.vectorPrimos[aux]), tag="numeritos")
                aux = aux + 1
        else:
            # Se pintan los primeros 12
            aux = 0
            for i in range(12):
                self.tela.create_text(self.posNumerosCinta[aux]+20,
                 165,
                  text=str(self.vectorPrimos[aux]), tag="numeritos")
                 
                aux = aux + 1

        # Se procede a pintar una leyenda
        aux = 0
        for i in range(1, 13):
            self.tela.create_text(self.posNumerosCinta[aux]+20,
                 200,
                  text=str(i), tag="leyenda")
            aux = aux + 1

    """Este metodo actualiza la lista de primos que se muestran
    spc puede ser: +12 o -12 para moverse a la der o izq
    """
    def actualizarListaPrimos(self, spc):
        # Si esta entre 0 y el tamano del vector
        if len(self.vectorPrimos)>self.posPintar+spc>=0:
            # se actualiza el puntero
            # Esta sera la nueva posA a pintar
            self.posPintar = self.posPintar + spc
            # Se captura el siguiente paquete de numeros
            paquete = []
            if self.posPintar+12<len(self.vectorPrimos):
                # Esto Siginifica que se pueden pintar 12 posiciones
                for i in range(self.posPintar, self.posPintar+12):
                    paquete.append(self.vectorPrimos[i])
                
               
            else:
                # Esto significa que quedan menos de 12 numeros para pintar
                for i in range(self.posPintar, len(self.vectorPrimos)):
                    paquete.append(self.vectorPrimos[i])    


            # Ya se capturo el vector de los sig primos a mostar procedo actualizar
            aux = 0
            for i in self.tela.find_withtag("numeritos"):
                if aux < len(paquete):
                    self.tela.itemconfigure(i, text=str(paquete[aux]))
                    aux = aux + 1
                else:
                    self.tela.itemconfigure(i, text="X")

            # Se procede a actualizar la leyenda
            for i in self.tela.find_withtag("leyenda"):
                # Capturo el elemento actual
                nro = int(self.tela.itemcget(i, 'text'))
                # lo actulizo sumandole spc
                nro = nro + spc
                self.tela.itemconfigure(i, text=str(nro))

        # Ojo: si no hay nada mas atras se borra el btn
        # Si hay algo adelante se pinta el btn
        if self.posPintar<12:
            self.borrarBTNPrevius()
        else:
            self.pintarBtnPrevius()

        # Ojo si no hay nada mas adelante se borra el btn
        # Si hay cosas por ver adelante se pinta
        if self.posPintar+12>=len(self.vectorPrimos):
            self.borrarBTNNext()
        else:
            self.pintarBtnNext()


# se instancia
s = Software()