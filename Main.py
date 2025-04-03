import tkinter as tk
from tkinter import ttk, messagebox, font
import random
import os
import re

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        self.root.configure(bg="#f0f0f0")
        
        # Custom colors
        self.primary_color = "#3498db"
        self.secondary_color = "#2980b9"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        self.text_color = "#2c3e50"
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.header_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=12)
        self.small_font = font.Font(family="Helvetica", size=10)
        
        # Title
        title_frame = tk.Frame(self.root, bg=self.primary_color, pady=10)
        title_frame.pack(fill=tk.X)
        
        title = tk.Label(title_frame, text="Billing System", 
                         font=self.title_font, bg=self.primary_color, fg="white")
        title.pack()
        
        # Variables
        self.initialize_variables()
        
        # Customer Details Frame
        self.create_customer_frame()
        
        # Product Frames
        self.create_product_frames()
        
        # Bill Area
        self.create_bill_area()
        
        # Bottom Frame
        self.create_bottom_frame()
        
        # Welcome Bill
        self.welcome_bill()
    
    def initialize_variables(self):
        # Medical
        self.sanitizer = tk.IntVar()
        self.mask = tk.IntVar()
        self.hand_gloves = tk.IntVar()
        self.syrup = tk.IntVar()
        self.cream = tk.IntVar()
        self.thermal_gun = tk.IntVar()
        
        # Grocery
        self.rice = tk.IntVar()
        self.food_oil = tk.IntVar()
        self.wheat = tk.IntVar()
        self.spices = tk.IntVar()
        self.flour = tk.IntVar()
        self.maggi = tk.IntVar()
        
        # Cold Drinks
        self.sprite = tk.IntVar()
        self.mineral = tk.IntVar()
        self.juice = tk.IntVar()
        self.coke = tk.IntVar()
        self.lassi = tk.IntVar()
        self.mountain_duo = tk.IntVar()
        
        # Total product price
        self.medical_price = tk.StringVar()
        self.grocery_price = tk.StringVar()
        self.cold_drinks_price = tk.StringVar()
        
        # Customer
        self.c_name = tk.StringVar()
        self.c_phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = tk.StringVar()
        
        # Tax
        self.medical_tax = tk.StringVar()
        self.grocery_tax = tk.StringVar()
        self.cold_drinks_tax = tk.StringVar()
    
    def create_customer_frame(self):
        F1 = tk.LabelFrame(self.root, text="Customer Details", font=self.header_font, 
                          bd=5, relief=tk.GROOVE, bg=self.bg_color, fg=self.text_color)
        F1.place(x=0, y=80, relwidth=1)
        
        # Customer Name
        cname_lbl = tk.Label(F1, text="Customer Name:", font=self.normal_font, 
                            bg=self.bg_color, fg=self.text_color)
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = tk.Entry(F1, width=15, textvariable=self.c_name, 
                            font=self.normal_font, bd=3, relief=tk.GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)
        
        # Customer Phone
        cphn_lbl = tk.Label(F1, text="Customer Phone:", font=self.normal_font, 
                           bg=self.bg_color, fg=self.text_color)
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = tk.Entry(F1, width=15, textvariable=self.c_phone, 
                           font=self.normal_font, bd=3, relief=tk.GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)
        cphn_txt.bind('<KeyRelease>', self.validate_phone)
        
        # Bill Number
        c_bill_lbl = tk.Label(F1, text="Bill Number:", font=self.normal_font, 
                             bg=self.bg_color, fg=self.text_color)
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = tk.Entry(F1, width=15, textvariable=self.search_bill, 
                             font=self.normal_font, bd=3, relief=tk.GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)
        c_bill_txt.bind('<KeyRelease>', self.validate_bill_number)
        
        # Search Button
        search_btn = tk.Button(F1, text="Search", command=self.find_bill, width=10, bd=3, 
                              font=self.normal_font, bg=self.secondary_color, fg="white",
                              activebackground=self.primary_color, activeforeground="white")
        search_btn.grid(row=0, column=6, pady=5, padx=10)
    
    def create_product_frames(self):
        # Medical Frame
        F2 = tk.LabelFrame(self.root, text="Medical Products", font=self.header_font, 
                          bd=5, relief=tk.GROOVE, bg=self.bg_color, fg=self.text_color)
        F2.place(x=5, y=180, width=325, height=380)
        
        # Medical Products
        self.create_product_entry(F2, "Sanitizer", self.sanitizer, 0)
        self.create_product_entry(F2, "Mask", self.mask, 1)
        self.create_product_entry(F2, "Hand Gloves", self.hand_gloves, 2)
        self.create_product_entry(F2, "Syrup", self.syrup, 3)
        self.create_product_entry(F2, "Cream", self.cream, 4)
        self.create_product_entry(F2, "Thermal Gun", self.thermal_gun, 5)
        
        # Grocery Frame
        F3 = tk.LabelFrame(self.root, text="Grocery Items", font=self.header_font, 
                          bd=5, relief=tk.GROOVE, bg=self.bg_color, fg=self.text_color)
        F3.place(x=340, y=180, width=325, height=380)
        
        # Grocery Products
        self.create_product_entry(F3, "Rice", self.rice, 0)
        self.create_product_entry(F3, "Food Oil", self.food_oil, 1)
        self.create_product_entry(F3, "Wheat", self.wheat, 2)
        self.create_product_entry(F3, "Spices", self.spices, 3)
        self.create_product_entry(F3, "Flour", self.flour, 4)
        self.create_product_entry(F3, "Maggi", self.maggi, 5)
        
        # Cold Drinks Frame
        F4 = tk.LabelFrame(self.root, text="Cold Drinks", font=self.header_font, 
                          bd=5, relief=tk.GROOVE, bg=self.bg_color, fg=self.text_color)
        F4.place(x=670, y=180, width=325, height=380)
        
        # Cold Drinks Products
        self.create_product_entry(F4, "Sprite", self.sprite, 0)
        self.create_product_entry(F4, "Mineral Water", self.mineral, 1)
        self.create_product_entry(F4, "Juice", self.juice, 2)
        self.create_product_entry(F4, "Coke", self.coke, 3)
        self.create_product_entry(F4, "Lassi", self.lassi, 4)
        self.create_product_entry(F4, "Mountain Duo", self.mountain_duo, 5)
    
    def create_product_entry(self, parent, label_text, variable, row):
        label = tk.Label(parent, text=label_text, font=self.normal_font, 
                        bg=self.bg_color, fg=self.text_color)
        label.grid(row=row, column=0, padx=10, pady=10, sticky='w')
        
        entry = tk.Entry(parent, width=10, textvariable=variable, 
                        font=self.normal_font, bd=3, relief=tk.GROOVE)
        entry.grid(row=row, column=1, padx=10, pady=10)
        entry.bind('<KeyRelease>', self.validate_number_input)
    
    def create_bill_area(self):
        F5 = tk.Frame(self.root, bd=5, relief=tk.GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
        
        bill_title = tk.Label(F5, text="Bill Area", font=self.header_font, bd=3, relief=tk.GROOVE)
        bill_title.pack(fill=tk.X)
        
        scroll_y = tk.Scrollbar(F5, orient=tk.VERTICAL)
        self.txtarea = tk.Text(F5, yscrollcommand=scroll_y.set, font=self.small_font)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=tk.BOTH, expand=1)
    
    def create_bottom_frame(self):
        F6 = tk.LabelFrame(self.root, text="Bill Summary", font=self.header_font, 
                          bd=5, relief=tk.GROOVE, bg=self.bg_color, fg=self.text_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        
        # Medical Price
        m1_lbl = tk.Label(F6, text="Total Medical Price", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='w')
        m1_txt = tk.Entry(F6, width=18, textvariable=self.medical_price, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m1_txt.grid(row=0, column=1, padx=18, pady=1)
        
        # Grocery Price
        m2_lbl = tk.Label(F6, text="Total Grocery Price", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_txt = tk.Entry(F6, width=18, textvariable=self.grocery_price, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m2_txt.grid(row=1, column=1, padx=18, pady=1)
        
        # Cold Drinks Price
        m3_lbl = tk.Label(F6, text="Total Cold Drinks Price", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_txt = tk.Entry(F6, width=18, textvariable=self.cold_drinks_price, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m3_txt.grid(row=2, column=1, padx=18, pady=1)
        
        # Medical Tax
        m4_lbl = tk.Label(F6, text="Medical Tax", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='w')
        m4_txt = tk.Entry(F6, width=18, textvariable=self.medical_tax, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m4_txt.grid(row=0, column=3, padx=18, pady=1)
        
        # Grocery Tax
        m5_lbl = tk.Label(F6, text="Grocery Tax", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='w')
        m5_txt = tk.Entry(F6, width=18, textvariable=self.grocery_tax, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m5_txt.grid(row=1, column=3, padx=18, pady=1)
        
        # Cold Drinks Tax
        m6_lbl = tk.Label(F6, text="Cold Drinks Tax", font=self.normal_font, 
                         bg=self.bg_color, fg=self.text_color)
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='w')
        m6_txt = tk.Entry(F6, width=18, textvariable=self.cold_drinks_tax, 
                         font=self.small_font, bd=3, relief=tk.GROOVE, state='readonly')
        m6_txt.grid(row=2, column=3, padx=18, pady=1)
        
        # Buttons
        btn_f = tk.Frame(F6, bd=3, relief=tk.GROOVE)
        btn_f.place(x=760, width=580, height=105)
        
        # Total Button
        total_btn = tk.Button(btn_f, command=self.total, text="Total", 
                             bg=self.primary_color, fg="white", pady=15, width=12, 
                             font=self.normal_font, bd=0)
        total_btn.grid(row=0, column=0, padx=5, pady=5)
        
        # Generate Bill Button
        generateBill_btn = tk.Button(btn_f, command=self.bill_area, text="Generate Bill", 
                                    bg=self.primary_color, fg="white", pady=15, width=12, 
                                    font=self.normal_font, bd=0)
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)
        
        # Clear Button
        clear_btn = tk.Button(btn_f, command=self.clear_data, text="Clear", 
                             bg=self.primary_color, fg="white", pady=15, width=12, 
                             font=self.normal_font, bd=0)
        clear_btn.grid(row=0, column=2, padx=5, pady=5)
        
        # Exit Button
        exit_btn = tk.Button(btn_f, command=self.exit_app, text="Exit", 
                            bg=self.accent_color, fg="white", pady=15, width=12, 
                            font=self.normal_font, bd=0)
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
    
    def validate_number_input(self, event):
        """Validate that only numbers are entered in quantity fields"""
        widget = event.widget
        content = widget.get()
        
        # Remove any non-digit characters
        if content and not content.isdigit():
            # Remove leading zeros
            cleaned_content = ''.join(filter(str.isdigit, content))
            # Remove leading zeros
            if cleaned_content:
                cleaned_content = str(int(cleaned_content))
                widget.delete(0, tk.END)
                widget.insert(0, cleaned_content)
            else:
                widget.delete(0, tk.END)
    
    def validate_phone(self, event):
        """Validate phone number input"""
        content = self.c_phone.get()
        if content and not content.isdigit():
            # Keep only digits
            cleaned_content = ''.join(filter(str.isdigit, content))
            self.c_phone.set(cleaned_content)
    
    def validate_bill_number(self, event):
        """Validate bill number input"""
        content = self.search_bill.get()
        if content and not content.isdigit():
            # Keep only digits
            cleaned_content = ''.join(filter(str.isdigit, content))
            self.search_bill.set(cleaned_content)
    
    def total(self):
        # Medical prices
        self.m_h_g_p = self.hand_gloves.get() * 12
        self.m_s_p = self.sanitizer.get() * 2
        self.m_m_p = self.mask.get() * 5
        self.m_sy_p = self.syrup.get() * 30
        self.m_c_p = self.cream.get() * 5
        self.m_t_g_p = self.thermal_gun.get() * 15
        self.total_medical_price = float(self.m_m_p + self.m_h_g_p + self.m_s_p + 
                                        self.m_c_p + self.m_t_g_p + self.m_sy_p)
        
        self.medical_price.set("Rs. " + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set("Rs. " + str(self.c_tax))
        
        # Grocery prices
        self.g_r_p = self.rice.get() * 10
        self.g_f_o_p = self.food_oil.get() * 10
        self.g_w_p = self.wheat.get() * 10
        self.g_s_p = self.spices.get() * 6
        self.g_f_p = self.flour.get() * 8
        self.g_m_p = self.maggi.get() * 5
        self.total_grocery_price = float(self.g_r_p + self.g_f_o_p + self.g_w_p + 
                                        self.g_s_p + self.g_f_p + self.g_m_p)
        
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.05), 2)  # Fixed tax calculation
        self.grocery_tax.set("Rs. " + str(self.g_tax))
        
        # Cold drinks prices
        self.c_d_s_p = self.sprite.get() * 10
        self.c_d_w_p = self.mineral.get() * 10
        self.c_d_j_p = self.juice.get() * 10
        self.c_d_c_p = self.coke.get() * 10
        self.c_d_l_p = self.lassi.get() * 10
        self.c_m_d = self.mountain_duo.get() * 10
        self.total_cold_drinks_price = float(self.c_d_s_p + self.c_d_w_p + self.c_d_j_p + 
                                           self.c_d_c_p + self.c_d_l_p + self.c_m_d)
        
        self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. " + str(self.c_d_tax))
        
        self.total_bill = float(self.total_medical_price + self.total_grocery_price + 
                               self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)
    
    def welcome_bill(self):
        self.txtarea.delete('1.0', tk.END)
        self.txtarea.insert(tk.END, "\t  Welcome to Billing Retail\n")
        self.txtarea.insert(tk.END, "\t    Your Shopping Partner\n")
        self.txtarea.insert(tk.END, f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(tk.END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(tk.END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(tk.END, f"\n=======================================")
        self.txtarea.insert(tk.END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(tk.END, f"\n=======================================")
    
    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are required")
        elif (self.medical_price.get() == "" or self.medical_price.get() == "Rs. 0.0") and \
             (self.grocery_price.get() == "" or self.grocery_price.get() == "Rs. 0.0") and \
             (self.cold_drinks_price.get() == "" or self.cold_drinks_price.get() == "Rs. 0.0"):
            messagebox.showerror("Error", "No product selected")
        else:
            self.welcome_bill()
            
            # Medical products
            if self.sanitizer.get() != 0:
                self.txtarea.insert(tk.END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
            if self.mask.get() != 0:
                self.txtarea.insert(tk.END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(tk.END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
            if self.syrup.get() != 0:
                self.txtarea.insert(tk.END, f"\n Syrup\t\t{self.syrup.get()}\t\t{self.m_sy_p}")
            if self.cream.get() != 0:
                self.txtarea.insert(tk.END, f"\n Cream\t\t{self.cream.get()}\t\t{self.m_c_p}")
            if self.thermal_gun.get() != 0:
                self.txtarea.insert(tk.END, f"\n Thermal Gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_g_p}")
            
            # Grocery products
            if self.rice.get() != 0:
                self.txtarea.insert(tk.END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(tk.END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(tk.END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.spices.get() != 0:
                self.txtarea.insert(tk.END, f"\n Spices\t\t{self.spices.get()}\t\t{self.g_s_p}")
            if self.flour.get() != 0:
                self.txtarea.insert(tk.END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
            if self.maggi.get() != 0:
                self.txtarea.insert(tk.END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
            
            # Cold drinks products
            if self.sprite.get() != 0:
                self.txtarea.insert(tk.END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
            if self.mineral.get() != 0:
                self.txtarea.insert(tk.END, f"\n Mineral\t\t{self.mineral.get()}\t\t{self.c_d_w_p}")
            if self.juice.get() != 0:
                self.txtarea.insert(tk.END, f"\n Juice\t\t{self.juice.get()}\t\t{self.c_d_j_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(tk.END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
            if self.lassi.get() != 0:
                self.txtarea.insert(tk.END, f"\n Lassi\t\t{self.lassi.get()}\t\t{self.c_d_l_p}")
            if self.mountain_duo.get() != 0:
                self.txtarea.insert(tk.END, f"\n Mountain Duo\t\t{self.mountain_duo.get()}\t\t{self.c_m_d}")
            
            self.txtarea.insert(tk.END, f"\n---------------------------------------")
            
            # Taxes
            if self.medical_tax.get() != "" and self.medical_tax.get() != "Rs. 0.0":
                self.txtarea.insert(tk.END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
            if self.grocery_tax.get() != "" and self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(tk.END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != "" and self.cold_drinks_tax.get() != "Rs. 0.0":
                self.txtarea.insert(tk.END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")
            
            self.txtarea.insert(tk.END, f"\n Total Bill:\t\t\t Rs. {self.total_bill:.2f}")
            self.txtarea.insert(tk.END, f"\n---------------------------------------")
            
            self.save_bill()
    
    def save_bill(self):
        # Create bills directory if it doesn't exist
        if not os.path.exists("bills"):
            os.makedirs("bills")
            
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', tk.END)
            try:
                f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving bill: {str(e)}")
        else:
            return
    
    def find_bill(self):
        if not self.search_bill.get():
            messagebox.showerror("Error", "Please enter bill number")
            return
            
        if not os.path.exists("bills"):
            messagebox.showerror("Error", "No bills found")
            return
            
        found = False
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                try:
                    f1 = open(f"bills/{i}", "r")
                    self.txtarea.delete("1.0", tk.END)
                    for d in f1:
                        self.txtarea.insert(tk.END, d)
                    f1.close()
                    found = True
                except Exception as e:
                    messagebox.showerror("Error", f"Error reading bill: {str(e)}")
                break
                
        if not found:
            messagebox.showerror("Error", "Invalid Bill Number")
    
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear all data?")
        if op > 0:
            # Reset all product quantities
            # Medical
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.syrup.set(0)
            self.cream.set(0)
            self.thermal_gun.set(0)
            
            # Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.spices.set(0)
            self.flour.set(0)
            self.maggi.set(0)
            
            # Cold Drinks
            self.sprite.set(0)
            self.mineral.set(0)
            self.juice.set(0)
            self.coke.set(0)
            self.lassi.set(0)
            self.mountain_duo.set(0)
            
            # Reset prices and taxes
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            
            # Reset customer details
            self.c_name.set("")
            self.c_phone.set("")
            
            # Generate new bill number
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.welcome_bill()
    
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

# Create bills directory if it doesn't exist
if not os.path.exists("bills"):
    os.makedirs("bills")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = Bill_App(root)
    root.mainloop()
