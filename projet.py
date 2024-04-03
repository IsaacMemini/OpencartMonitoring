from tkinter import *
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from function import *


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
       ##corps
        self.titre = Label(self.entete,text = "Monitoring Page",font=("sans serif",23,"bold"),fg="#ffffff",bg="#1e91cf")
        self.titre.place(x=10,y=10)
        self.corp2 = Frame(self.root, bg="#1b80c2")
        self.corp2.place(x=315, y=83, width=230, height=120)
        self.entete2 = Frame(self.corp2,bg="#1e91cf")
        self.entete2.place(width=230,height=35)
        self.entete2Label1 = Label(self.entete2,text="TOTAL ORDERS",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete2Label1.place(x=5,y=5)
        self.corp2Label = Label(self.corp2,text=numberOfConversion(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp2Label.place(x=95,y=55)
        self.corp3 = Frame(self.root, bg="#1b80c2")
        self.corp3.place(x=562, y=83, width=230, height=120)
        self.entete3 = Frame(self.corp3,bg="#1e91cf")
        self.entete3.place(width=230,height=35)
        self.entete3Label1 = Label(self.entete3,text="NB OF TRANSACTIONS",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete3Label1.place(x=5,y=5)
        self.corp3Label = Label(self.corp3,text=activeShoppingSession(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp3Label.place(x=100,y=55)
        self.corp4 = Frame(self.root, bg="#1b80c2") 
        self.corp4.place(x=809, y=83, width=230, height=120)
        self.entete4 = Frame(self.corp4,bg="#1e91cf")
        self.entete4.place(width=230,height=35)
        self.entete4Label1 = Label(self.entete4,text="TOTAL CUSTOMERS",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete4Label1.place(x=5,y=5)
        self.corp4Label = Label(self.corp4,text=totalCustomers(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp4Label.place(x=105,y=55)
        self.corp5 = Frame(self.root, bg="#1b80c2")
        self.corp5.place(x=1056, y=83, width=188, height=120)
        self.entete5 = Frame(self.corp5,bg="#1e91cf")
        self.entete5.place(width=230,height=35)
        self.entete5Label1 = Label(self.entete5,text="PEOPLE ONLINE",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete5Label1.place(x=5,y=5)
        self.corp5Label = Label(self.corp5,text=peopleOnline(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp5Label.place(x=80,y=55)
        self.corp6 = Frame(self.root, bg="#1b80c2")
        self.corp6.place(x=1056, y=220, width=188, height=120)
        self.entete6 = Frame(self.corp6,bg="#1e91cf")
        self.entete6.place(width=230,height=35)
        self.entete6Label1 = Label(self.entete6,text="CUSTOMER RETENTION RATE",font=("sans serif",9,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete6Label1.place(x=5,y=5)
        self.corp6Label = Label(self.corp6,text=customerRetentionRate(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp6Label.place(x=80,y=55)
        self.corp7 = Frame(self.root, bg="#1b80c2")
        self.corp7.place(x=809, y=220, width=230, height=120)
        self.entete7 = Frame(self.corp7,bg="#1e91cf")
        self.entete7.place(width=230,height=35)
        self.entete7Label1 = Label(self.entete7,text="TOTAL SALES",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete7Label1.place(x=5,y=5)
        self.corp7Label = Label(self.corp7,text=totalSales(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp7Label.place(x=80,y=55)
        self.corp8 = Frame(self.root, bg="#1b80c2")
        self.corp8.place(x=562, y=220, width=230, height=120)
        self.entete8 = Frame(self.corp8,bg="#1e91cf")
        self.entete8.place(width=230,height=35)
        self.entete8Label1 = Label(self.entete8,text="Revenue",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete8Label1.place(x=5,y=5)
        self.corp8Label = Label(self.corp8,text=revenue(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp8Label.place(x=100,y=55)
        self.corp9 = Frame(self.root, bg="#1b80c2")
        self.corp9.place(x=315, y=220, width=230, height=120)
        self.entete9 = Frame(self.corp9,bg="#1e91cf")
        self.entete9.place(width=230,height=35)
        self.entete9Label1 = Label(self.entete9,text="ABANDONED CART",font=("sans serif",11,"bold"),fg="#ffffff",bg="#1e91cf")
        self.entete9Label1.place(x=5,y=5)
        self.corp9Label = Label(self.corp9,text=abandonedCart(),font=("sans serif",25,"bold"),fg="#ffffff",bg="#1b80c2")
        self.corp9Label.place(x=95,y=55)
        self.signatureText = Label(self.FrameMenu,text="CREATED BY",font=("sans serif",11,"bold"),fg="#000000",bg="#ffffff")
        self.signatureText.place(x=15,y=400)
        self.signatureText1 = Label(self.FrameMenu,text="Isaac Memini Edou ",font=("sans serif",11,"bold"),fg="#000000",bg="#ffffff")
        self.signatureText1.place(x=15,y=430)
        self.signatureText2 = Label(self.FrameMenu,text="Ousmane Ali Brahim ",font=("sans serif",11,"bold"),fg="#000000",bg="#ffffff")
        self.signatureText2.place(x=15,y=460)
        self.signatureText3 = Label(self.FrameMenu,text="Mamadou Abdoul Hamid DIALLO",font=("sans serif",11,"bold"),fg="#000000",bg="#ffffff")
        self.signatureText3.place(x=15,y=490)
          ##bouton de sortie
        self.logOut = Button(self.FrameMenu,bd=0,text="Quit",bg="#ffffff",font=("sans serif",13,"bold"),command=self.root.quit) 
        self.logOut.place(x=25,y=650,width=265)
        self.sortieImage = Image.open(r"arrow.png")
        photo = ImageTk.PhotoImage(self.sortieImage)
        self.logo = Label(self.FrameMenu,image = photo,bg="#ffffff")
        self.logo.image3 = photo
        self.logo.place(x=20,y=650)
        
        self.corp1 = Frame(self.root, bg="#ffffff")
        self.corp1.place(x=315, y=357, width=930, height=300)
if __name__ == "__main__":
    root = Tk()
    DashboardOpencart(root)
    root.mainloop()