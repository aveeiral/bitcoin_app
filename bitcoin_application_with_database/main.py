# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:04:12 2020

@author: Aviral Gaur
"""
import requests
import json
from tkinter import *
import sqlite3 as sq
from tkinter import messagebox
from tkinter import Menu

#request is used to get the data from the url
#json is to store the data in aparseable form
  
conn = sq.connect('coin.db')
obj = conn.cursor()

obj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
conn.commit()

#obj.execute("INSERT INTO coin VALUES(1, 'BTC', 2, 3200)")
#conn.commit()

#obj.execute("INSERT INTO coin VALUES(2, 'EOS', 3, 2.05)")
#conn.commit()

#obj.execute("INSERT INTO coin VALUES(3, 'ETH', 4, 75)")
#conn.commit()

#obj.execute("INSERT INTO coin VALUES(4, 'XRP', 10, 82)")
#conn.commit()


def reset():
    for frame in tk.winfo_children():
        frame.destroy()
    
    app_nav()
    my_appln()
    app_header()
              

def app_nav():
    
    def clear_all():
        obj.execute("DELETE FROM coin")
        conn.commit()
        
        messagebox.showinfo("Bitcoin Notification"," All coins deleted ---ADD COINS")
        reset()
    
    def close_app():
        tk.destroy()
        
    
    
    my_menu = Menu(tk)
    
    file_item = (Menu)(my_menu)
    file_item.add_command(label='clear bitcoin application', command=clear_all)
    file_item.add_command(label='close application', command=close_app)
    my_menu.add_cascade(label="File", menu=file_item)
    
    
    edit_item = (Menu)(my_menu)
    edit_item.add_command(label='Indent')
    edit_item.add_command(label='Unindent')
    my_menu.add_cascade(label="Edit", menu=edit_item)
    
    view_item = (Menu)(my_menu)
    view_item.add_command(label='Toolbars')
    view_item.add_command(label='Debugging')
    my_menu.add_cascade(label="View", menu=view_item)
    
    
    
    help_item = (Menu)(my_menu)
    help_item.add_command(label='Check For Updates')
    help_item.add_command(label='Close All')
    my_menu.add_cascade(label="Help", menu=help_item)
    
    
    tk.config(menu=my_menu)


def my_appln():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=INR&CMC_PRO_API_KEY=3e0a0b55-350c-4e1a-8828-83e8f7efdb67")
    api = json.loads(api_request.content)


#    coins =[
#            {
#            "symbol":"BTC",
#            "amount_owned": 2,
#            "price_per_coin": 3200
#        },
#        {
#            "symbol":"EOS",
#            "amount_owned": 3,
#            "price_per_coin": 2.05                
#        },
#        {
#            "symbol":"ETH",
#            "amount_owned":4,
#            "price_per_coin": 75
#        },
#        {
#            "symbol":"XRP",
#            "amount_owned": 10,
#            "price_per_coin": 82
#            }
#        ] 
        
    obj.execute("SELECT * FROM coin")
    coins = obj.fetchall()        
    
    def font_colour(amount):
        if amount >= 0:
            return "green"
        else:
            return "red"
        
    def insert_coin():
        obj.execute("INSERT INTO coin(symbol, price, amount) VALUES(?, ?, ?)",(symbol_text.get(), amount_text.get(), price_text.get()))
        conn.commit()
        
        messagebox.showinfo("Bitcoin Notification", "Coin Added To Application Successfully")
        reset()
        

    def update_coin():
        obj.execute("UPDATE coin SET symbol=?, price=?, amount=? WHERE id=?", (symbol_update.get(), price_update.get(), amount_update.get(), bitcoinid_update.get()))
        conn.commit()
        
        messagebox.showinfo("Bitcoin Notification", "Coin Updated To Application Successfully")
        reset()
    
    
    def delete_coin():
        obj.execute("DELETE FROM coin WHERE id=?", (bitcoinid_delete.get(),))
        conn.commit()
        
        messagebox.showinfo("Bitcoin Notification", "Coin Deleted From Application Successfully")
        reset()
    
    
   
    total_pl = 0
    coin_row = 1
    tot_curr_value = 0
    total_amount_paid = 0
    
    
    for i in range(0, 300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin[1]:
                total_paid = coin[2]*coin[3]
                current_value = coin[2]*api["data"][i]["quote"]["INR"]["price"]
                pl_percoin = api["data"][i]["quote"]["INR"]["price"] - coin[3]
                total_pl_coin = pl_percoin*coin[2]
                
                total_pl += total_pl_coin
                tot_curr_value += current_value
                total_amount_paid += total_paid
                #print(api["data"][i]["name"] + "--" + api["data"][i]["symbol"])
                #print("price -${0:.2f}".format(api["data"][i]["quote"]["INR"]["price"]))
                #print("Number of coins :", coin[2])
                #print("total amount paid :", "${0:.2f}".format(total_paid))
                #print("current_value :", "${0:.2f}".format(current_value))
                #print("P/L per coin :", "${0:.2f}".format(pl_percoin))
                #print("Total pl coin :", "${0:.2f}".format(total_pl_coin))
                
                
                #print("-----------------")
                
                bitcoin_id = Label(tk, text=coin[0], bg="tomato", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
                bitcoin_id.grid(row=coin_row, column=0, sticky=N+S+E+W)
                
                name = Label(tk, text=api["data"][i]["symbol"], bg="beige", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=4, sticky=N+S+E+W)
    
                price = Label(tk, text=api["data"][i]["quote"]["INR"]["price"], bg="beige", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=8, sticky=N+S+E+W)
    
                no_coins = Label(tk, text=int(coin[2]), bg="beige", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=16, sticky=N+S+E+W)
                
                p_per_coin = Label(tk, text=coin[3], bg="beige", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                p_per_coin.grid(row=coin_row, column=12, sticky=N+S+E+W)

                amt_paid = Label(tk, text="${0:.2f}".format(total_paid), bg="beige", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                amt_paid.grid(row=coin_row, column=20, sticky=N+S+E+W)
    
                current_val = Label(tk, text="${0:.2f}".format(current_value), bg="beige", fg="black", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=24, sticky=N+S+E+W)
    
                pl_coin = Label(tk, text="${0:.2f}".format(pl_percoin), bg="beige", fg=font_colour(float("{0:.2f}".format(pl_percoin))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=28, sticky=N+S+E+W)
    
                totalpl = Label(tk, text="${0:.2f}".format(total_pl_coin), bg="beige", fg=font_colour(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=32, sticky=N+S+E+W)
                
                coin_row += 1
    #insert data
    symbol_text = Entry(tk, borderwidth=2, relief="groove")
    symbol_text.grid(row=coin_row+1, column=4)                             
    
    price_text = Entry(tk, borderwidth=2, relief="groove")
    price_text.grid(row=coin_row+1, column=16)
    
    amount_text = Entry(tk, borderwidth=2, relief="groove")
    amount_text.grid(row=coin_row+1, column=12)
     
    add_coin = Button(tk, text="Add Coin", bg="lawn green", fg="black", command=insert_coin, font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    add_coin.grid(row=coin_row+1, column=20, sticky=N+S+E+W)
    
    
    #update coin
    bitcoinid_update = Entry(tk, borderwidth=2, relief="groove")
    bitcoinid_update.grid(row=coin_row+2, column=0)
    
    symbol_update = Entry(tk, borderwidth=2, relief="groove")
    symbol_update.grid(row=coin_row+2, column=4)                             
    
    price_update = Entry(tk, borderwidth=2, relief="groove")
    price_update.grid(row=coin_row+2, column=12)
    
    amount_update = Entry(tk, borderwidth=2, relief="groove")
    amount_update.grid(row=coin_row+2, column=16)
    
    update_coin_text = Button(tk, text="Update Coin", bg="lawn green", fg="black", command=update_coin, font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    update_coin_text.grid(row=coin_row+2, column=20, sticky=N+S+E+W)
    
    
    #delete coin
    bitcoinid_delete = Entry(tk, borderwidth=2, relief="groove")
    bitcoinid_delete.grid(row=coin_row+3, column=0)
    
    delete_coin_text = Button(tk, text="Delete Coin", bg="red", fg="black", command=delete_coin, font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    delete_coin_text.grid(row=coin_row+3, column=16, sticky=N+S+E+W)
    
    
    
    
    
    totalap = Label(tk, text="${0:.2f}".format(total_amount_paid), bg="black", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    totalap.grid(row=coin_row, column=20, sticky=N+S+E+W)
    
    totalcv = Label(tk, text="${0:.2f}".format(tot_curr_value), bg="black", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=24, sticky=N+S+E+W)
    
    totalpl = Label(tk, text="${0:.2f}".format(total_pl), bg="black", fg=font_colour(float("{0:.2f}".format(total_pl))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    totalpl.grid(row=coin_row, column=32, sticky=N+S+E+W)   
    
    api = ""
    
    refresh = Button(tk, text="Refresh", bg="SeaGreen1", fg="black", command=reset, font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    refresh.grid(row=coin_row+1, column=32, sticky=N+S+E+W)   
             

tk= Tk()
tk.title("BITCOIN DASHBOARD")
tk.iconbitmap("fav.ico")

def app_header():
    bitcoin_id = Label(tk, text="Bitcoin id", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    bitcoin_id.grid(row=0, column=0, sticky=N+S+E+W)
    
    name = Label(tk, text="Coin Name", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    name.grid(row=0, column=4, sticky=N+S+E+W)
    
    price = Label(tk, text="Price", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    price.grid(row=0, column=8, sticky=N+S+E+W)
    
    no_coins = Label(tk, text="Price Per Coin", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    no_coins.grid(row=0, column=12, sticky=N+S+E+W)
    
    p_per_coin = Label(tk, text="Coin Owned", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    p_per_coin.grid(row=0, column=16, sticky=N+S+E+W)
    
    amt_paid = Label(tk, text="Total Amount Paid", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    amt_paid.grid(row=0, column=20, sticky=N+S+E+W)
    
    current_val = Label(tk, text="Current Value", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    current_val.grid(row=0, column=24, sticky=N+S+E+W)
    
    pl_coin = Label(tk, text="profit/loss per coin", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    pl_coin.grid(row=0, column=28, sticky=N+S+E+W)
    
    totalpl = Label(tk, text="Total profit/loss with coin", bg="azure2", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl.grid(row=0, column=32, sticky=N+S+E+W)

    
app_nav()
app_header()            
my_appln()    

tk.mainloop()

obj.close()
conn.close()

print("donee")





   
    
    
    







