import random
import commands

quotesFile = open('Quotes.txt', 'r')
quotesAsString = quotesFile.read();

quotesArray = str.split(quotesAsString, "\n")

sel = random.randint(0,len(quotesArray))

selQuote = quotesArray[sel];

selQuote = str.replace(selQuote, "\"", "\'")
selQuote = str.replace(selQuote, "#", "\t-")

output = commands.getoutput("defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText \"" + selQuote + "\"")
print output
