class User:
    # print("spread smile")
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.followers += 1

use = User("001", "Amrutraj Halageri")
use2 = User("002", "Savitri Halageri")

use.follow(use2)
print(use.followers)