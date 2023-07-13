class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # !You can make a default value that they start with that is not apart of the parameters 
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Deni")
user_2 = User("002", "Mark")

user_2.follow(user_1)

# print(user_1.username)
# print(user_2.id)
# print(user_1.followers)
print(user_1.followers)
print(user_2.following)