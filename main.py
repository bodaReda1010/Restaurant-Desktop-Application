from tkinter import * 
from tkinter import messagebox
from datetime import date
import database


app = Tk()
app.title("Boda's Restaurant")
app.geometry('900x350+200+150')
app.config(bg = '#0A0B0C')
app.resizable(False , False)
app.iconbitmap('resturant.ico')


def receipt():
    meals_entries = [chesseburger_entry,machromburger_entry,smachburgersingle_entry,smachburgerdouble_entry,smachburgertrible_entry,chikenburger_entry,frenchfries_entry]
    drinks_entries = [cola_entry,sprite_entry,icecofe_entry,blueberry_entry,latte_entry,lemon_entry,orange_entry]
    meals_prices , drinks_prices = database.get_product_prices()

    try:
        meals_quantities = []
        for entry in meals_entries:
            text = entry.get()
            if text:
                meals_quantities.append(int(text))
            else:
                meals_quantities.append(0)

        drinks_quantities = []
        for entry in drinks_entries:
            text = entry.get()
            if text:
                drinks_quantities.append(int(text))
            else:
                drinks_quantities.append(0)

        meals_total = sum(quantity * price for quantity , price in zip(meals_quantities , meals_prices))
        drinks_total = sum(quantity * price for quantity , price in zip(drinks_quantities , drinks_prices))
        total = meals_total + drinks_total
        todays_date = date.today().strftime('%d %m %Y')
        if total == 0:
            messagebox.showerror('Error' , 'Choose At Least 1 Product')
        else:
            mealstotallabel.configure(text = f'Meals Total: {meals_total}$')
            drinkstotallabel.configure(text = f'Drinks Total: {drinks_total}$')
            totallabel.configure(text = f'Total: {total}$')
            datelabel.configure(text = f"Toda's Day: {todays_date}")
            return meals_total , drinks_total , total , todays_date
    except ValueError:
        messagebox.showerror('Error' , 'Entered Values Should Be Integers')

def new():
    chesseburger_entry.delete(0,END)
    machromburger_entry.delete(0,END)
    smachburgersingle_entry.delete(0,END)
    smachburgerdouble_entry.delete(0,END)
    smachburgertrible_entry.delete(0,END)
    chikenburger_entry.delete(0,END)
    frenchfries_entry.delete(0,END)
    cola_entry.delete(0,END)
    sprite_entry.delete(0,END)
    icecofe_entry.delete(0,END)
    blueberry_entry.delete(0,END)
    latte_entry.delete(0,END)
    lemon_entry.delete(0,END)
    orange_entry.delete(0,END)
    mealstotallabel.configure(text = '')
    drinkstotallabel.configure(text = '')
    totallabel.configure(text = '')
    datelabel.configure(text = '')

def save():
    totals = receipt()
    if totals is not None:
        meals_total , drinks_total , total , todays_date = totals
        with open('Reciept.txt' , 'a+') as file:
            file.write(f'Meals Total: {meals_total}$\n')
            file.write(f'Drinks Total: {drinks_total}$\n')
            file.write(f'Total: {total}$\n')
            file.write(f"Date: {todays_date}\n===========================\n")
        messagebox.showinfo('Success' , 'Receipt Has Been Saved')


#----------------------------Food Frame------------------------------------
meals_frame = Frame(app , bg = '#1B2631' , width = 300 , height = 350)
meals_frame.place(x = 0 , y = 0)

meals_label = Label(meals_frame , text = 'Food' , font = ('Palatino Linotype' , 15) , bg = '#1B2631' , fg = '#EBDEF0')
meals_label.place(x = 120 , y = 0)

line_label = Label(meals_frame , text = '--------------------' , font = ('Palatino Linotype' , 15)  , bg = '#1B2631' , fg = '#EBDEF0')
line_label.place(x = 80 , y = 25)

chesseburger_label = Label(meals_frame , text = 'Cheese Burger' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
chesseburger_label.place(x = 0 , y = 75)

machromburger_label = Label(meals_frame , text = 'Machrom Burger' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
machromburger_label.place(x = 0 , y = 115)

smachburgersingle_label = Label(meals_frame , text = 'Smach Burger(Single)' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
smachburgersingle_label.place(x = 0 , y = 155)

smachburgerdouble_label = Label(meals_frame , text = 'Smach Burger(Double)' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
smachburgerdouble_label.place(x = 0 , y = 195)

smachburgertrible_label = Label(meals_frame , text = 'Smach Burger(Trible)' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
smachburgertrible_label.place(x = 0 , y = 235)

chikenburger_label = Label(meals_frame , text = 'Chiken Burger' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
chikenburger_label.place(x = 0 , y = 275)

frenchfries_label = Label(meals_frame , text = 'French Fries' , font = ('Palatino Linotype' , 12) , bg = '#1B2631' , fg = '#EBDEF0')
frenchfries_label.place(x = 0 , y = 315)

chesseburger_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
chesseburger_entry.place(x = 125 , y = 82)

machromburger_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
machromburger_entry.place(x = 127 , y = 120)

smachburgersingle_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
smachburgersingle_entry.place(x = 168 , y = 162 , width = 80 , height = 20)

smachburgerdouble_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
smachburgerdouble_entry.place(x = 168 , y = 200 , width = 80 , height = 20)

smachburgertrible_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
smachburgertrible_entry.place(x = 168 , y = 240 , width = 80 , height = 20)

chikenburger_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
chikenburger_entry.place(x = 120 , y = 280)

frenchfries_entry = Entry(meals_frame , bd = 2 , justify = 'center' , bg = 'white')
frenchfries_entry.place(x = 120 , y = 320)

#----------------------------Drink Frame------------------------------------
drinksframe = Frame(app , bg = '#273746' , width = 300 , height = 350)
drinksframe.place(x = 260 , y = 0)

drinks_label = Label(drinksframe , text = 'Drink' , font = ('Palatino Linotype' , 15)  , bg = '#273746' , fg = '#EBDEF0')
drinks_label.place(x = 120 , y = 0)

line_label = Label(drinksframe , text = '------------------' , font = ('Palatino Linotype' , 15)  , bg = '#273746' , fg = '#EBDEF0')
line_label.place(x = 95 , y = 25)

cola_label = Label(drinksframe , text = 'Cola' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
cola_label.place(x = 0 , y = 75) 

sprite_label = Label(drinksframe , text = 'Sprite' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
sprite_label.place(x = 0 , y = 115)

icecofe_label = Label(drinksframe , text = 'Ice Coffee' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
icecofe_label.place(x = 0 , y = 155)

blueberry_label = Label(drinksframe , text = 'Blue Berry' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
blueberry_label.place(x = 0 , y = 195)

latte_label = Label(drinksframe , text = 'Latte' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
latte_label.place(x = 0 , y = 235)

lemon_label = Label(drinksframe , text = 'Lemon' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
lemon_label.place(x = 0 , y = 275)

Orange_label = Label(drinksframe , text = 'Orange' , bg = '#273746' , fg = '#EBDEF0' , font = ('Palatino Linotype' , 15) )
Orange_label.place(x = 0 , y = 315)

cola_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
cola_entry.place(x = 160 , y = 82)

sprite_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
sprite_entry.place(x = 160 , y = 120)

icecofe_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
icecofe_entry.place(x = 160 , y = 160)

blueberry_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
blueberry_entry.place(x = 160 , y = 200)

latte_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
latte_entry.place(x = 160 , y = 240)

lemon_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
lemon_entry.place(x = 160 , y = 280)

orange_entry = Entry(drinksframe , bd = 2 , justify = 'center' , bg = 'white')
orange_entry.place(x = 160 , y = 320)

#----------------------------Receipt Frame------------------------------------

receiptframe = Frame(app , bg = '#34495E' , width = 340 , height = 230)
receiptframe.place(x = 560 , y = 0)

receiptlabel = Label(receiptframe , text = 'Receipt' , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
receiptlabel.place(x = 120 , y = 0)

receiptlabel = Label(receiptframe , text = '---------------' , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
receiptlabel.place(x = 110 , y = 27)

mealstotallabel = Label(receiptframe , text = '' , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
mealstotallabel.place(x = 0 , y = 50)

drinkstotallabel = Label(receiptframe , text = '' , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
drinkstotallabel.place(x = 0 , y = 90)

totallabel = Label(receiptframe , text = '' , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
totallabel.place(x = 0 , y = 130)

datelabel = Label(receiptframe , text = "" , font = ('Palatino Linotype' , 15)  , bg = '#34495E' , fg = '#EBDEF0')
datelabel.place(x = 0 , y = 170)

#----------------------------buttons Frame------------------------------------

buttonsframe = Frame(app , bg = '#1B2631' , width = 340 , height = 120)
buttonsframe.place(x = 560 , y = 230)

#----------------------------Buttons------------------------------------

receiptbutton = Button(buttonsframe , text = 'Receipt' , bg = '#2874A6' , fg = '#FBFCFC' , font = ('Monotype Corsiva' , 17) , command = receipt)
receiptbutton.place(x = 30 , y = 10 , width = 100 , height = 38)

savebutton = Button(buttonsframe , text = 'Save' , bg = '#16A085' , fg = '#FBFCFC' , font = ('Monotype Corsiva' , 17) , command = save)
savebutton.place(x = 200 , y = 10 , width = 100 , height = 38)

newbutton = Button(buttonsframe , text = 'New' , bg = '#C0392B' , fg = '#FBFCFC' , font = ('Monotype Corsiva' , 17) , command = new)
newbutton.place(x = 120 , y = 70 , width = 100 , height = 38)

app.mainloop()