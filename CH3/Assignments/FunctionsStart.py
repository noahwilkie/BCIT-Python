import urllib.request

#Prints a display message on the display
def intro():
    print()
    print("##########################################################")
    print("#                                                        #")
    print("#                Welcome User!                           #")
    print("#  This program will tell you the undiscounted price     #")
    print("#      of beans and the discounted price of beans        #")
    print("#                                                        #")
    print("##########################################################")
    print()

#Retrives the current price of coffee beans from the url
def currentPrice():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return str((text[start_of_price:end_of_price]))

#Takes 10% off of the value in the parameter of the discountedPrice() function call
def discountedPrice(price):
    sale = price / 10.0
    salepriceprice = price - sale
    return salepriceprice

#Calls the function intro()
intro()

#Assigns the returned value from currentPrice() to cprice and displays it to the display
cprice = currentPrice()
print()
print("The undiscounted price of beans is $" + (cprice))

#Assigns the returned value from discountPrice() to dprice and displays it to the display
dprice = discountedPrice(float(cprice))
dprice = str(dprice)[0:4]
print()
print("The discounted price of beans is $" + dprice)
