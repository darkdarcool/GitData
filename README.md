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