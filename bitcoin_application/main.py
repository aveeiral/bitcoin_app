# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:04:12 2020

@author: Aviral Gaur
"""
import requests
import json
from tkinter import *

#request is used to get the data from the url
#json is to store the data in aparseable form
                
def font_colour(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_appln():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=INR&CMC_PRO_API_KEY=3e0a0b55-350c-4e1a-8828-83e8f7efdb67")
    api = json.loads(api_request.content)


    coins =[
            {
            "symbol":"BTC",
            "amount_owned": 2,
            "price_per_coin": 3200
        },
        {
            "symbol":"EOS",
            "amount_owned": 3,
            "price_per_coin": 2.05                
        },
        {
            "symbol":"ETH",
            "amount_owned":4,
            "price_per_coin": 75
        },
        {
            "symbol":"XRP",
            "amount_owned": 10,
            "price_per_coin": 82
            }
        ] 
        
        
        

   
    total_pl = 0
    coin_row = 1
    tot_curr_value = 0
    for i in range(0, 300):
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"]*coin["price_per_coin"]
                current_value = coin["amount_owned"]*api["data"][i]["quote"]["INR"]["price"]
                pl_percoin = api["data"][i]["quote"]["INR"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin*coin["amount_owned"]
                
                total_pl = total_pl + total_pl_coin
                tot_curr_value = tot_curr_value +current_value
                
                #print(api["data"][i]["name"] + "--" + api["data"][i]["symbol"])
                #print("price -${0:.2f}".format(api["data"][i]["quote"]["INR"]["price"]))
                #print("Number of coins :", coin["amount_owned"])
                #print("total amount paid :", "${0:.2f}".format(total_paid))
                #print("current_value :", "${0:.2f}".format(current_value))
                #print("P/L per coin :", "${0:.2f}".format(pl_percoin))
                #print("Total pl coin :", "${0:.2f}".format(total_pl_coin))
                
                
                #print("-----------------")
                
                name = Label(tk, text=api["data"][i]["symbol"], bg="purple", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)
    
                price = Label(tk, text=api["data"][i]["quote"]["INR"]["price"], bg="black", fg="white", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=4, sticky=N+S+E+W)
    
                no_coins = Label(tk, text=coin["amount_owned"], bg="purple", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=8, sticky=N+S+E+W)
                
                p_per_coin = Label(tk, text=coin["price_per_coin"], bg="black", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                p_per_coin.grid(row=coin_row, column=12, sticky=N+S+E+W)

                amt_paid = Label(tk, text="${0:.2f}".format(total_paid), bg="purple", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                amt_paid.grid(row=coin_row, column=16, sticky=N+S+E+W)
    
                current_val = Label(tk, text="${0:.2f}".format(current_value), bg="black", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=20, sticky=N+S+E+W)
    
                pl_coin = Label(tk, text="${0:.2f}".format(pl_percoin), bg="purple", fg=font_colour(float("{0:.2f}".format(pl_percoin))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=24, sticky=N+S+E+W)
    
                totalpl = Label(tk, text="${0:.2f}".format(total_pl_coin), bg="black", fg=font_colour(float("{0:.2f}".format(total_pl_coin))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=28, sticky=N+S+E+W)
                
                coin_row = coin_row + 1
                                

    totalcv = Label(tk, text="${0:.2f}".format(tot_curr_value), bg="black", fg="white", font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=20, sticky=N+S+E+W)
    
    totalpl = Label(tk, text="${0:.2f}".format(total_pl), bg="black", fg=font_colour(float("{0:.2f}".format(total_pl))), font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    totalpl.grid(row=coin_row, column=28, sticky=N+S+E+W)   
    
    api = ""
    
    update = Button(tk, text="Update", bg="yellow", fg="black", command=my_appln, font="Lato 12", padx="2", pady="2", borderwidth=2, relief="groove")
    update.grid(row=coin_row+1, column=28, sticky=N+S+E+W)   
             

tk= Tk()
tk.title("BITCOIN DASHBOARD")
tk.iconbitmap("fav.ico")


name = Label(tk, text="Coin Name", bg="blue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(tk, text="Price", bg="black", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=4, sticky=N+S+E+W)

no_coins = Label(tk, text="Coin Ownned", bg="blue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
no_coins.grid(row=0, column=8, sticky=N+S+E+W)

p_per_coin = Label(tk, text="Price Per Coin", bg="black", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
p_per_coin.grid(row=0, column=12, sticky=N+S+E+W)

amt_paid = Label(tk, text="Total Amount Paid", bg="blue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
amt_paid.grid(row=0, column=16, sticky=N+S+E+W)

current_val = Label(tk, text="Current Value", bg="black", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
current_val.grid(row=0, column=20, sticky=N+S+E+W)

pl_coin = Label(tk, text="profit/loss per coin", bg="blue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=24, sticky=N+S+E+W)

totalpl = Label(tk, text="Total profit/loss with coin", bg="black", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
totalpl.grid(row=0, column=28, sticky=N+S+E+W)

    
            
my_appln()    

tk.mainloop()
print("donee")





