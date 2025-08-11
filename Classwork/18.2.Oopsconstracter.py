class Instagram:
    def __init__(self, username, password):
        print("Welcome to Instagram")
        self._bio = ''                       # protected
        self.post = []                       # public list
        self.followers = []                  # public list (changed from dict)
        self.following = []                  # public list (changed from dict)
        self.username = username             # public
        self.__password = password           # private
        print(f"Hello {self.username}, login successful")

    @property
    def externalbio(self):
        return self._bio

    @externalbio.setter
    def externalbio(self, upd_bio):
        self._bio = upd_bio

    def showpassword(self):
        return self.__password

    def updatepassword(self, new_pwd):
        self.__password = new_pwd
        return "Password updated successfully"


# Create object
Tharuni = Instagram("tharuni", "sree@123!")

# public var-accessing
print("Bio:", Tharuni.externalbio)
print("Post:", Tharuni.post)
print("Followers:", Tharuni.followers)
print("Following:", Tharuni.following)
print("Username:", Tharuni.username)

# modify public vars
Tharuni.externalbio = "Peaceful"
Tharuni.post.append("python-course.png")
Tharuni.followers.extend(["sreevachala", "Vidhya", "vilok"])
Tharuni.following.extend(["samatha", "sreenivasulu", "chaithanya"])
Tharuni.username = "Tharuni_."

print("\nAfter updating:")
print("Bio:", Tharuni.externalbio)
print("Post:", Tharuni.post)
print("Followers:", Tharuni.followers)
print("Following:", Tharuni.following)
print("Username:", Tharuni.username)

# private var-accessing
print("\nPassword:", Tharuni.showpassword())
print("Updated password:", Tharuni.updatepassword("Tharuni@123"))
print("New password:", Tharuni.showpassword())

#Output
'''Welcome to Instagram
Hello tharuni, login successful
Bio:
Post: []
Followers: []
Following: []
Username: tharuni

After updating:
Bio: Peaceful
Post: ['python-course.png']
Followers: ['sreevachala', 'Vidhya', 'vilok']
Following: ['samatha', 'sreenivasulu', 'chaithanya']
Username: Tharuni_.

Password: sree@123!
Updated password: Password updated successfully
New password: Tharuni@123
'''



#Example
class login:
    def __init__(self, username, password):
        self.username = username       # public
        self.__password = password     # private
        self._otp = 1234               # protected

    def getpassword(self):
        return self.__password

    def updatepassword(self, new_pwd):
        self.__password = new_pwd

    @property
    def publicotp(self):
        return self._otp

    @publicotp.setter
    def publicotp(self, new_otp):
        self._otp = new_otp


# Create object
sreevachala = login("sreevachala", "password123")

# public
print("Username:", sreevachala.username)  

# private (access via method)
print("Password:", sreevachala.getpassword())

# protected (access via property)
print("OTP:", sreevachala.publicotp)

# update public
sreevachala.username = "_sreevachala_"
print("Updated username:", sreevachala.username)

# update private
sreevachala.updatepassword("sree@123!")
print("Updated password:", sreevachala.getpassword())

# update protected
sreevachala.publicotp = 1111
print("Updated OTP:", sreevachala.publicotp)

#output
'''
Username: sreevachala
Password: password123
OTP: 1234
Updated username: _sreevachala_
Updated password: sree@123!
Updated OTP: 1111
'''



