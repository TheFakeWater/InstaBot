from instabot import Bot

bot = Bot()
bot.login("yourusernamehere", "yourpasswordhere")  # Don't forget to put your password and username !

hashtags = ["starwars", "starwarsfan", "anakinskywalker", "prequels", "originals"]  # Edit your hashtags
while True:
    # Follow people
    for hashtag in hashtags:
        users = bot.get_hashtag_users(hashtag)
        bot.follow_users(users)
        bot.like_hashtag(hashtag)
        bot.max_following_to_followers_ratio(50)  # Ratio Following/Followers
