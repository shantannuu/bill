import tkinter
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x800+0+0")
        self.root.title("Billing Software")
        
        title = tkinter.Label(self.root,text="BILLING HERE",font=("times new roman",30,"bold"),bg="black",fg="white",pady=2,bd=12,relief="solid")
        title.pack(fill= "x")

        # VARIABLES
        #food
        self.c_drink=tkinter.IntVar() 
        self.maggie=tkinter.IntVar()
        self.goodday=tkinter.IntVar()
        self.snacks=tkinter.IntVar()
        self.lays=tkinter.IntVar()
        #cosmetics
        self.soap=tkinter.IntVar()
        self.paste=tkinter.IntVar()
        self.detergent=tkinter.IntVar()
        self.shampoo=tkinter.IntVar()
        self.brush=tkinter.IntVar()
        #total products
        self.cosmetic_price = tkinter.StringVar()
        self.food_price = tkinter.StringVar()
        self.drinks_price = tkinter.StringVar()
        self.cosmetic_tax = tkinter.StringVar()
        self.food_tax = tkinter.StringVar()
        self.drinks_tax = tkinter.StringVar()
        #customer
        self.c_name = tkinter.StringVar()
        self.c_phone = tkinter.StringVar()
        
        self.c_bill= tkinter.StringVar()
        x=random.randint(1000,9999)
        self.c_bill.set(str(x))
        self.search_bill = tkinter.StringVar()
        

        f1 = tkinter.LabelFrame(self.root,text="customer Details",bg="black",font=("times new roman",15,"bold"),fg="white",bd=5)
        f1.place(x=0,y=70,relwidth=1)
        
        name = tkinter.Label(f1,text="Customer Name",font=("times new roman",18,"bold"),bg="black",fg="white")
        name.grid(row=0,column=0,padx=20,pady=5)

        name_txt = tkinter.Entry(f1,font=("times new roman",15),width=20,textvariable=self.c_name).grid(row=0,column=1,padx=10,pady=5)

        phone = tkinter.Label(f1,text="Phone Number",font=("times new roman",18,"bold"),bg="black",fg="white")
        phone.grid(row=0,column=2,padx=20,pady=5)

        phone_txt = tkinter.Entry(f1,font=("times new roman",15),width=16,textvariable=self.c_phone).grid(row=0,column=3,padx=10,pady=5)

        bill = tkinter.Label(f1,text="Bill Number",font=("times new roman",18,"bold"),bg="black",fg="white")
        bill.grid(row=0,column=4,padx=20,pady=5)

        bill_txt = tkinter.Entry(f1,font=("times new roman",15),width=16,textvariable=self.search_bill).grid(row=0,column=5,padx=10,pady=5)

        btn = tkinter.Button(f1,text="Search",command=self.find_bill,width=20,bd=7,font=("times new roman",15,"bold"),pady=4).grid(row=0,column=6,padx=10,pady=5)

        f2 = tkinter.LabelFrame(self.root,text="Food",bg="black",font=("times new roman",15,"bold"),fg="white",bd=5)
        f2.place(x=0,y=135,width=325,height=380)

        cold_drink = tkinter.Label(f2,text="Cold Drink",font=("times new roman",16,"bold"),bg="black",fg="white")
        cold_drink.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        cold_drink_txt = tkinter.Entry(f2,font=("times new roman",15),width=16,textvariable=self.c_drink).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        maggie = tkinter.Label(f2,text="Maggie",font=("times new roman",16,"bold"),bg="black",fg="white")
        maggie.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        maggie_txt = tkinter.Entry(f2,font=("times new roman",15),width=16,textvariable=self.maggie).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        Good_day = tkinter.Label(f2,text="Good Day",font=("times new roman",16,"bold"),bg="black",fg="white")
        Good_day.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        Good_day_txt = tkinter.Entry(f2,font=("times new roman",15),width=16,textvariable=self.goodday).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        snacks = tkinter.Label(f2,text="Snacks",font=("times new roman",16,"bold"),bg="black",fg="white")
        snacks.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        snacks_txt = tkinter.Entry(f2,font=("times new roman",15),width=16,textvariable=self.snacks).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        lays = tkinter.Label(f2,text="Lays",font=("times new roman",16,"bold"),bg="black",fg="white")
        lays.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        lays_txt = tkinter.Entry(f2,font=("times new roman",15),width=16,textvariable=self.lays).grid(row=4,column=1,padx=10,pady=10,sticky="w")


        f3 = tkinter.LabelFrame(self.root,text="cosmetics",bg="black",font=("times new roman",15,"bold"),fg="white",bd=5)
        f3.place(x=325,y=135,width=325,height=380)

        soap = tkinter.Label(f3,text="Bath Soap",font=("times new roman",16,"bold"),bg="black",fg="white")
        soap.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        soap_txt = tkinter.Entry(f3,font=("times new roman",15),width=16,textvariable=self.soap).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        paste = tkinter.Label(f3,text="Tooth Paste",font=("times new roman",16,"bold"),bg="black",fg="white")
        paste.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        paste_txt = tkinter.Entry(f3,font=("times new roman",15),width=16,textvariable=self.paste).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        detergent = tkinter.Label(f3,text="Detergent",font=("times new roman",16,"bold"),bg="black",fg="white")
        detergent.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        detergent_txt = tkinter.Entry(f3,font=("times new roman",15),width=16,textvariable=self.detergent).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        shampoo = tkinter.Label(f3,text="Shampoo",font=("times new roman",16,"bold"),bg="black",fg="white")
        shampoo.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        shampoo_txt = tkinter.Entry(f3,font=("times new roman",15),width=16,textvariable=self.shampoo).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        brush = tkinter.Label(f3,text="Brush ",font=("times new roman",16,"bold"),bg="black",fg="white")
        brush .grid(row=4,column=0,padx=20,pady=10,sticky="w")

        brush_txt = tkinter.Entry(f3,font=("times new roman",15),width=16,textvariable=self.brush).grid(row=4,column=1,padx=10,pady=10,sticky="w")


        f4 = tkinter.LabelFrame(self.root,text="Cold Drinks",bg="black",font=("times new roman",15,"bold"),fg="white",bd=5)
        f4.place(x=650,y=135,width=325,height=380)

        Limpka = tkinter.Label(f4,text="Limpka",font=("times new roman",16,"bold"),bg="black",fg="white")
        Limpka.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        Limpka_txt = tkinter.Entry(f4,font=("times new roman",15),width=16).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        thumb_up = tkinter.Label(f4,text="Thumb Up",font=("times new roman",16,"bold"),bg="black",fg="white")
        thumb_up.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        thumb_up_txt = tkinter.Entry(f4,font=("times new roman",15),width=16).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        fruity = tkinter.Label(f4,text="fruity",font=("times new roman",16,"bold"),bg="black",fg="white")
        fruity.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        fruity_txt = tkinter.Entry(f4,font=("times new roman",15),width=16).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        maza = tkinter.Label(f4,text="Maza",font=("times new roman",16,"bold"),bg="black",fg="white")
        maza.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        maza_txt = tkinter.Entry(f4,font=("times new roman",15),width=16).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        sprite = tkinter.Label(f4,text="Sprite",font=("times new roman",16,"bold"),bg="black",fg="white")
        sprite.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        sprite_txt = tkinter.Entry(f4,font=("times new roman",15),width=16).grid(row=4,column=1,padx=10,pady=10,sticky="w")

        f5 = tkinter.Frame(self.root,bd=10,relief="groove")
        f5.place(x=980,y=135,width=440,height=380)

        bill_title=tkinter.Label(f5,text="Bill Here",font=("times new roman",20,"bold"),bd=4,relief="solid").pack(fill="x")

        scroll_y=tkinter.Scrollbar(f5,orient="vertical")
        self.textarea = tkinter.Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right",fill="y")
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill="both",expand=1)

        f6 = tkinter.LabelFrame(self.root,text="Bill Menu",bg="black",font=("times new roman",18,"bold"),fg="white",bd=5)
        f6.place(x=0,y=520,relwidth=1,height=240)

        cosmetic_price = tkinter.Label(f6,text="Total Cosmetic Price",font=("times new roman",16,"bold"),bg="black",fg="white")
        cosmetic_price.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        cosmetic_price_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.cosmetic_price).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        Food_price = tkinter.Label(f6,text="Total Food Price",font=("times new roman",16,"bold"),bg="black",fg="white")
        Food_price.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        Food_price_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.food_price).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        drink_price = tkinter.Label(f6,text="Total Drink Price",font=("times new roman",16,"bold"),bg="black",fg="white")
        drink_price.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        drink_price_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.drinks_price).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        cosmetic_tax = tkinter.Label(f6,text="Total Cosmetic Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
        cosmetic_tax.grid(row=0,column=3,padx=20,pady=10,sticky="w")

        cosmetic_tax_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.cosmetic_tax).grid(row=0,column=4,padx=10,pady=10,sticky="w")

        Food_tax = tkinter.Label(f6,text="Total Food Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
        Food_tax.grid(row=1,column=3,padx=20,pady=10,sticky="w")

        Food_tax_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.food_tax).grid(row=1,column=4,padx=10,pady=10,sticky="w")

        drink_tax = tkinter.Label(f6,text="Total Drink Tax",font=("times new roman",16,"bold"),bg="black",fg="white")
        drink_tax.grid(row=2,column=3,padx=20,pady=10,sticky="w")

        drink_tax_txt = tkinter.Entry(f6,font=("times new roman",15),width=16,textvariable=self.drinks_tax).grid(row=2,column=4,padx=10,pady=10,sticky="w")

        btn_f=tkinter.Frame(f6,bd=5)
        btn_f.place(x=750,y=7,width=640,height=130)

        btn_total=tkinter.Button(btn_f,command=self.total,text="Total",pady=25,width=15,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=0,padx=5,pady=10)

        Gbill_total=tkinter.Button(btn_f,command=self.bill_area,text="Generate Bill",pady=25,width=15,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=1,padx=5,pady=10)
        
        clear_total=tkinter.Button(btn_f,text="Clear",pady=25,width=15,font=("times new roman",15,"bold"),bd=5).grid(row=0,column=2,padx=5,pady=10)
        
        exit_total=tkinter.Button(btn_f,text="Exit",pady=25,width=15,font=("times new roman",15,
        "bold"),bd=5).grid(row=0,column=3,padx=5,pady=10)
        self.welcome_Bill()
    
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_sh_p=self.shampoo.get()*40
        self.c_d_p=self.detergent.get()*40
        self.c_b_p=self.brush.get()*40
        self.c_p_p=self.paste.get()*40
        self.total_cosmetic = float(
                                        self.c_s_p+
                                        self.c_sh_p+
                                        self.c_d_p+
                                        self.c_b_p+
                                        self.c_p_p
                                    )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic))
        self.c_tax = round((self.total_cosmetic*0.05),2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))
        
        self.c_c_p=self.c_drink.get()*40
        self.c_g_p=self.goodday.get()*40
        self.c_sn_p=self.snacks.get()*40
        self.c_m_p=self.maggie.get()*40
        self.c_l_p=self.lays.get()*40
        self.total_food = float(
                                        self.c_c_p
                                        +self.c_g_p
                                        +self.c_sn_p
                                        +self.c_m_p
                                        +self.c_l_p
                                    )
        self.food_price.set("Rs. " + str(self.total_food))
        self.f_tax = round((self.total_food*0.10),2)
        self.food_tax.set("Rs. " + str(self.f_tax))
        
        self.total_bill=float(self.total_cosmetic+self.total_food+self.f_tax+self.c_tax)
        
    def welcome_Bill(self):
        self.textarea.delete('1.0',tkinter.END)
        self.textarea.insert(tkinter.END,"\t\tWelcome shantanu patil\n")
        self.textarea.insert(tkinter.END,f"\n Bill Number : {self.c_bill.get()}")
        self.textarea.insert(tkinter.END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(tkinter.END,f"\n Customer Phone Number : {self.c_phone.get()}")
        self.textarea.insert(tkinter.END,"\n\n *****************************************************")
        self.textarea.insert(tkinter.END,f"\n Products\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(tkinter.END,"\n *****************************************************")
    
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            tkinter.messagebox.showerror("Error","Customer Details are Must")
        elif self.cosmetic_price.get()=="Rs. 0.0" or self.food_price.get()=="Rs. 0.0" or self.cosmetic_tax.get()=="Rs. 0.0" or self.food_tax.get()=="Rs. 0.0":
             tkinter.messagebox.showerror("Error","No product selected")
        else:
            self.welcome_Bill()
            if self.soap.get()!=0:
                self.textarea.insert(tkinter.END,f"\n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s_p}")
            if self.shampoo.get()!=0:
                self.textarea.insert(tkinter.END,f"\n Shampoo\t\t\t{self.shampoo.get()}\t\t\t{self.c_sh_p}")
            if self.detergent.get()!=0:
                self.textarea.insert(tkinter.END,f"\n Detergent\t\t\t{self.detergent.get()}\t\t\t{self.c_d_p}")
            if self.brush.get()!=0:
                self.textarea.insert(tkinter.END,f"\n Brush\t\t\t{self.brush.get()}\t\t\t{self.c_b_p}")
            if self.paste.get()!=0:
                self.textarea.insert(tkinter.END,f"\n Tooth Paste\t\t\t{self.paste.get()}\t\t\t{self.c_p_p}")
            self.textarea.insert(tkinter.END,"\n\n -----------------------------------------------------")
            
            if self.cosmetic_price.get()!="Rs. 0.0":
                self.textarea.insert(tkinter.END,f"\n Cosmetic Tax\t\t\t\t\t\t{self.cosmetic_tax.get()}")
            if self.food_price.get()!="Rs. 0.0":
                self.textarea.insert(tkinter.END,f"\n Food Tax\t\t\t\t\t\t{self.food_tax.get()}")

            self.textarea.insert(tkinter.END,"\n -----------------------------------------------------")   
            self.textarea.insert(tkinter.END,f"\n Total Bill :\t\t\t\t\t\tRs.{self.total_bill}")
            self.textarea.insert(tkinter.END,"\n -----------------------------------------------------")
            self.save_bill()
        
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.textarea.get("1.0",tkinter.END)
            f1=open("bills/"+str(self.c_bill.get())+str(self.c_name.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.c_bill.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete("1.0",tkinter.END)
                for d in f1:
                    self.textarea.insert(tkinter.END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("ERROR","Invalid bill no.")

root = tkinter.Tk()
obj = Bill_App(root)

root.mainloop()