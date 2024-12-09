# A Python Program (Email Slicer)

# Taking input from user
email=input("Enter the Email ID:").strip()  

# Finding username
Username=email[: email.index("@")]

# Find Domain Name
Domain=email[email.index("@")+1:]

print("Your user name is:" ,Username)
print("Domain Name is:" ,Domain)    
