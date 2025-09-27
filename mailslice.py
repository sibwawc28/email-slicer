print("Hey queen, enter your mail so that I can slice it ")
email=input()

if "@" not in email:   
    print("Invalid email")
    exit()

words=email.split('@')
username=words[0]
dom_ext=words[1]  #domain and extension
next=dom_ext.split('.')
domain=next[0]
extension=next[1]

print(f"The username is {username}")
print(f"The domain is {domain}")
print(f"The extension is {extension}")


#can also use:
#if email.count('@')!=1: exit()