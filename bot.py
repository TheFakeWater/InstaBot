
from instabot import Bot

bot = Bot()
bot.login("yourusernamehere", "yourpasswordhere")
#Check


hashtags = ["starwars", "starwarsfan", "anakinskywalker", "prequels", "originals"]  # Edit your hashtags
while True:
    for hashtag in hashtags:
        users = bot.get_hashtag_users(hashtag)
        bot.follow_users(users)
        bot.like_hashtag(hashtag)
