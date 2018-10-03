import urllib.request

def intro():
    print("Welcome!")
    print("This program will tell you the current price of coffee beans")
    print("I hope it works")

def currentPrice():
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return(text[start_of_price:end_of_price])

print()    
intro()
print()
undiscounted = currentPrice()
print("The undiscounted price of beans is $" + undiscounted)