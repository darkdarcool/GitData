from GitData import parse, readUser 
user = readUser("darkdarcool")
user = parse(user)
print(user.raw())