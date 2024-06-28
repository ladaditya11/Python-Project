#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import tkinter as tk

class RMS:
    def __init__(self, restaurant_name, restaurant_menu):
        self.bill = 0
        self.rest_name = restaurant_name
        self.menu = restaurant_menu
        self.user_order = ''
        self.user_pay = 0
        self.order_li = []
        self.wlcm_msg = f'Welcome to {self.rest_name}'

    def welcome_user(self):
        print('Welcome to ', self.rest_name.title())
        print('*' * 30)
        
    def display_menu(self):
        print('Menu')
        for i in self.menu:
            print(i.title(), self.menu[i])
        print('*' * 30)
    
    def take_order(self):
        global user_order
        self.user_order = input('Please place your order here:')
    
    def prepare_order(self):
        print('Preparing your', self.user_order.title())
        import time
        time.sleep(0.5)
        self.order_li.append(self.user_order)
        self.bill = self.bill + self.menu[self.user_order.lower()]
    
    def serve_order(self):
        print('Your order is ready!')
        print('Please enjoy your', self.user_order.title())
    
    def display_bill(self):
        print('Total Bill:', self.bill)
        self.excel_bill = self.bill

    def verify_payment(self):
        self.user_pay = int(input('Please pay your bill here:'))
        while self.bill > self.user_pay:
            self.bill = self.bill - self.user_pay
            print('Payment Failed!')
            print('Please pay remaining', self.bill)
            self.user_pay = int(input('Please pay your bill here:'))
        if self.user_pay > self.bill:
            print('Here is your change:', self.user_pay - self.bill)
        else:
            pass

    def thank_user(self):
        print('Thank you visiting ', self.rest_name, 'Come back soon...')
        file_path = 'order history.xlsx'
        try:
            self.df = pd.read_excel(file_path)
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=['user order', 'total bill', 'date time'])
        
        row_number = len(self.df)
        from datetime import datetime
        self.curr_dt = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.df.loc[row_number] = [', '.join(self.order_li), self.excel_bill, self.curr_dt]
        self.df.to_excel(file_path, index=False)

    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.prepare_order()
            self.serve_order()
            self.user_repeat_order = input('Do you want to order more?')
            while self.user_repeat_order.lower() == 'yes':
                self.repeat_order()
                self.user_repeat_order = input('Do you want to order more?')
            self.display_bill()
            self.verify_payment()
            self.thank_user()
        else:
            print('Invalid Order')
            self.order_process()
    
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.prepare_order()
            self.serve_order()
        else:
            print('Invalid Order')
            self.repeat_order()

if __name__ == '__main__':
    file = open('user input.txt')
    user_input = file.readlines()
    
    rn = user_input[0].replace('\n', '')
    
    food_name = user_input[1].replace('\n', '').split(',')
    food_prices = [int(i) for i in user_input[2].split(',')]
    rm = dict(zip(food_name, food_prices))
    
    hotel = RMS(rn, rm)
    
    window = tk.Tk()
    window.geometry('500x500')
    window.title('RMS')
    tk.Label(window, text=hotel.wlcm_msg, font=('Helvetica', 18)).place(x=150, y=10)
    tk.Button(window, text='MENU', command=hotel.display_menu, width=20).place(x=150, y=100)
    tk.Button(window, text='START ORDER', command=hotel.order_process, width=20).place(x=150, y=150)
    window.mainloop()


# In[ ]:




