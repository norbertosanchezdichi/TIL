class Comment:
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes
        
c = Comment("davey123", "lol you're so silly", 3)
print(c.username)
print(c.text)
print(c.likes)

another_comment = Comment("rosa77", "soooo cute!!!")
print(another_comment.username)
print(another_comment.text)
print(another_comment.likes)