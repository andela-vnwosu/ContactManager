class Contact:
     def __init__(self, name, phonenumber, email, website, birthday):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.website = website
        self.birthday = birthday
        
    # def newContact(self):
    #     self.picture = True

AmakasContact = Contact("amaka", "08030972138", "amaka@me.com","www.me.com", "26-10-1987")
print(AmakasContact.name, AmakasContact.phonenumber, AmakasContact.email)
