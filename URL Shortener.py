# 1 Importing statement
 
import pyshorteners

# 2 Initialising the shortener

shortener = pyshorteners.Shortener()

# 3 Getting the url from the user

long_link = input(" Your link: ")

# 4 Generating the tiny url

short_link = shortener.tinyurl.short(long_link)

# 5 Displaying the tiny url

print(short_link)

