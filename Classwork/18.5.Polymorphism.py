'''Polymorphism = same name, many behaviors.
Types in Python:
Overloading (compile-time) → same function name, different arguments.
Overriding (run-time) → child class redefines parent method.
Duck Typing → object type doesn’t matter, only behavior matters.'''
#Method overriding
class Normaluser:
    def __init__(self,username):
        self.username=username
        print(f'\nWelcome to youtube\n{self.username} account is created')
    def playvideo(self):
        print("Ads Included")
        print("No Background play")
        print("Limited Content")
        print("Download with low quality")
        print("No youtube Music")
    def profile(self):
        print("you can upload your profile")
    def MultipleDevice(self):
        print("you can login with different devices")
    def Shorts(self):
        print("you can see many shorts")
    def likes(self):
        print("Likes")
    def share(self):
        print("Share")
    def subscribe(self):
        print("subscribe")
    def comment(self):
        print("comment")
class primiumuser(Normaluser):
    def __init__(self,username):
        super().__init__(username)
    def playvideo(self):
        print("Ads Free")
        print("Background play")
        print("Exclusive Content")
        print("Download with high quality")
        print("youtube Music is Available")
           

samatha=Normaluser("samatha")
samatha.playvideo()
samatha.profile()
samatha.MultipleDevice()
samatha.Shorts()
samatha.likes()
samatha.subscribe()
samatha.comment()
samatha.share()


sreenivasulu=primiumuser(Normaluser)
sreenivasulu.playvideo()
sreenivasulu.profile()
sreenivasulu.MultipleDevice()
sreenivasulu.Shorts()
sreenivasulu.likes()
sreenivasulu.subscribe()
sreenivasulu.comment()
sreenivasulu.share()


'''Welcome to youtube
(<__main__.Normaluser object at 0x000001A959F36A50>, 'samatha') account is created
Ads Included
No Background play
Limited Content
Download with low quality
No youtube Music
you can upload your profile
you can login with different devices
you can see many shorts
Likes
subscribe
comment
Share

Welcome to youtube
(<__main__.primiumuser object at 0x000001A959F36BA0>, <class '__main__.Normaluser'>) account is created
Ads Free
Background play
Exclusive Content
Download with high quality
youtube Music is Available
you can upload your profile
you can login with different devices
you can see many shorts
Likes
subscribe
comment
Share
'''
#Overloading 
class Number:
    def __init__(self,number):
        self.number=number
    def __add__(self,other):
        return self.number+other.number
    def __sub__(self,other):
        return self.number-other.number
    def __mul__(self,other):
        return self.number*other.number
    def __div__(self,other):
        return self.number/other.number
    def __eq__(self,other):
        return self.number==other.number
    def __gt__(self,other):
        return self.number>other.number
    def __lt__(self,other):
        return self.number<other.number
    
n1=(30)
n2=(28)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1>n2)
print(n1<n2)

'''58
2
840
1.0714285714285714
False
True
False'''

