import urllib.request
page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode("utf8")
#print(text)
print()
index = text.find("$")
begin = index + 1
end = index + 5
print(text[begin:end])