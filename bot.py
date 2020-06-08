from time import sleep
import secrets
from instabot import Bot

bot = Bot()
bot.login(secrets.Credentials.username, secrets.Credentials.password)  # Make a secret.py file and make a class
# Credentials then make two strings: username and password


hashtags = ["starwars", "starwarsfan", "anakinskywalker", "prequels", "originals"]  # Edit your hashtags
while True:
    for hashtag in hashtags:
        users = bot.get_hashtag_users(hashtag)
        bot.follow_users(users)
        bot.like_hashtag(hashtag)
