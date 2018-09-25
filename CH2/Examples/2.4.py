import urllib.request
page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
html = page.read().decode("utf8")

#Prints heading in Caps
headStart = html.find("Welcome")
headEnd = html.find("e</") + 1
headUp = html[headStart:headEnd].upper()
print()
print("Printing heading in all Capital letters: " + headUp)
print()

#replaces coffee with cocoa
specialStart = html.find("Special")
specialEnd = html.find("</strong")
specialRep = (html[specialStart:specialEnd].replace("coffee","cocoa").replace("<strong>",""))
print("Replacing coffee with cocoa: " + specialRep)
print()

#Determines if the text begins with <html> and ends with </html>
fileBegin = html.startswith("<html>")
fileEnd = html.endswith("</html>")

if fileBegin == True & fileEnd == True:
    print("This file starts with <html> and ends with </html>")
else:
    print("This file does not begin with <html> or ends with </html>")
