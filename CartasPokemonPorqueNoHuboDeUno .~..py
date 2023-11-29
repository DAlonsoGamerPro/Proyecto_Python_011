from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("JuegoCartasPokemonPorqueNoEncontréCartasDeUno")
root.geometry("600x400")
root.configure(background="saddle brown")

abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
bulbasour = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open ("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open ("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open ("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))





root.mainloop()