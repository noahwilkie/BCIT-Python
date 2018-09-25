import urllib.request
import time


price = 99.99
while price > 3.74:
    time.sleep(2)
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html") 
    text = page.read().decode("utf8") 
    where = text.find('>$') 
    start_of_price = where + 2 
    end_of_price = start_of_price + 4 
    price = text[start_of_price:end_of_price]
    price = float(price)
    print (price)
    

print("Buy")


#Use lines of code below to crreate a loop

#print("Buy")
#while price > 4.74:
#price = 99.99

