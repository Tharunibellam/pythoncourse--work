#super()=when where we have same method in the parents and child class the to extract parents class form child instead of writing the parent class name, we can just use super()
#Base calss _ Instagram story
class Instagramstory:
    def __init__(self,user):
        self.user = user
        print(f'\n {self.user} user is created')
        self.user_content =""
    def post_story(self,content):
        self.story_content = content
        return (f"{self.user} posted a story: {content}")
#Singal Inheritance - Add Like Feature
class storywithLikes(Instagramstory):
    def __init__(self, user):
        super().__init__(user)
        self.likes=0
    def like_story(self):
        self.likes += 1
        print(f"story liked! total likes: {self.likes}")
class storywithcomments(Instagramstory):
    def __init__(self,user):
        super().__init__(user)
        self.comments = []
    def add_comment(self, comment):
        self.comments.append(comment)
        print (f"New comment added: {comment}")


class storywithReactions(Instagramstory):
    def __init__(self, user):
        super().__init__(user)
        self.reactions = {"😂": 0, "❤": 0, "🔥": 0}
    def react_to_story(self, reaction):
        if reaction in self.reactions:
            self.reactions[reaction] += 1
            print(f"Reaction {reaction} added! Total: {self.reactions[reaction]}")
        else:
            print("Invalid reaction!")
class storywithcloseFriends(storywithLikes,storywithcomments,storywithReactions):
    def __init__(self,user):
        storywithLikes.__init__(self,user)
        storywithcomments.__init__(self,user)
        storywithReactions.__init__(self,user)
        self.close_friends_only = False
    def set_close_friends(self,status):
        self.close_friends_only = status
        mode = "close Friends" if status else "public"
        return f"story visibility set to: {mode}"

Tharuni = Instagramstory('Tharuni')
Tharuni.post_story('Tomorrowis holiday')

Indhu=storywithLikes('Indhu')
Indhu.post_story('saturday is also holiday')
Indhu.like_story()
Indhu.like_story()
Indhu.like_story()
Indhu.like_story()
Indhu.like_story()

chandhana = storywithcomments('chandhana')
chandhana.post_story('sunday is also holiday')
chandhana.add_comment("....")
chandhana.add_comment("Great")

Niharika=storywithReactions('Niharika')
Niharika.post_story('Monday is not holiday')
Niharika.react_to_story("😂")
Niharika.react_to_story("🔥")
Niharika.react_to_story("❤")
Niharika.react_to_story("😂")
Niharika.react_to_story("😂")
Niharika.react_to_story("❤")
Niharika.react_to_story("🔥")
Niharika.react_to_story("❤")

''' Tharuni user is created

 Indhu user is created
story liked! total likes: 1
story liked! total likes: 2
story liked! total likes: 3
story liked! total likes: 4
story liked! total likes: 5

 chandhana user is created
New comment added: ....
New comment added: Great

 Niharika user is created
Reaction 😂 added! Total: 1
Reaction 🔥 added! Total: 1
Reaction ❤ added! Total: 1
Reaction 😂 added! Total: 2
Reaction 😂 added! Total: 3
Reaction ❤ added! Total: 2
Reaction 🔥 added! Total: 2
Reaction ❤ added! Total: 3'''