# GitData

GitData can revieve the data for users and so much more coming soon! This can revolutionize flask, and Django websited by not using Github auth... just textbox auth! And using this module, you can get just as much data, way faster!

# Usage

It isn't the most simple to use, but it can be used very simply! Here is a sample on how to use it!

``` python
from GitData import readUser, parse 
user = readUser("darkdarcool") # You can change it to anyones username! 
user = parse(user) # Parse it 
print(user.username()) # Print the user's name!
```
Let's break it down. 
We first import the package, and then the initiate the `readUser` class. While it returns raw json, and you can use `user.raw_data()['dict_slices']`, we reccomend using our built in parser! Where we return the data to you! We initiate the parser overwriting the readUser class, because you don't really need it anymore! And then we can specify what data we want returned! We specify username, so then we initiate the function, and it will return the users username!