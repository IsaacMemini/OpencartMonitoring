from tkinter import *
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from function import *



cur.execute("SELECT value FROM `oc_setting` WHERE `key` LIKE 'payment_%_status' AND `value` LIKE '0' ")
if len(cur.fetchall()) != 0:
    state = 'unBlock'
else:
    state = 'Block'

def toBlockTransaction():
    global state
    cur.execute("SELECT value FROM `oc_setting` WHERE `key` LIKE 'payment_%_status' AND `value` LIKE '0' ")
    resultats = cur.fetchall()
    if len(resultats) != 0:
        cur.execute("UPDATE oc_setting SET value = '1' WHERE `key` LIKE 'payment_%_status' AND value = '0'")
        state = 'Block'
    else:
        cur.execute("UPDATE oc_setting SET value = '0' WHERE `key` LIKE 'payment_%_status' AND value = '1'")
        state = 'unBlock'
    conn.commit()

previousState = state
previousNumberOfConversion = numberOfConversion()
previousActiveShoppingSession = activeShoppingSession()
previousPeopleOnline = peopleOnline()
previousTotalCustomer = totalCustomers()
previousAbandonnedCard = abandonedCart()
previousRevenue = revenue()
previousTotalSales = totalSales()
previousCustomerRetentionRate = customerRetentionRate()
if totalCustomers()[0] != 0:
    peoplePercentage = peopleOnline()[0] * 100 / totalCustomers()[0]
else:
    peoplePercentage = 0
    
class DashboardOpencart:
    def __init__(self,root):
        self.root = root
        self.root.title("client Opencart")
        self.root.geometry("1399x768")
        self.root.config(bg="#eff5f6")
        ######En tete
        self.entete = Frame(self.root,bg="#1e91cf")
        self.entete.place(x = 300,y = 0,width=1070,height=60)
        self.deconnecte = Button(self.entete,text=state,bg="#ffffff",font=("sans serif",13,"bold"),bd=0,fg="#1e91cf",cursor="hand2",command=toBlockTransaction)
        self.deconnecte.place(x=850,y=15,width=100)
        #Menu
        self.FrameMenu = Frame(self.root,bg="#ffffff")
        self.FrameMenu.place(x=0,y=0,width=300,height=750)
        self.logoImage = Image.open(r"opencart-logo.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff" )
        self.logo.image1 = photo
        self.logo.place(x = 70,y=15)
        
        ##ajouter profil de l'administrateur
        self.profilImage = Image.open(r"avatar.ico")
        photo = ImageTk.PhotoImage(self.profilImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff" )
        self.logo.image2 = photo
        self.logo.place(y=100)
        self.Nom =Label(self.FrameMenu,text="Admin",bg="#ffffff",font=("sans serif",13,"bold"))
        self.Nom.place(x=90,y=350)
       
         
if __name__ == "__main__":
    root = Tk()
    DashboardOpencart(root)
    root.mainloop()