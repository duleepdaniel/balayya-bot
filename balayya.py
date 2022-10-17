import praw
import time
import random

reddit = praw.Reddit(
    client_id="XXX-YYY-ZZZZ",
    client_secret="XXX-YYY-ZZZZ",
    user_agent="Comment Extraction (by u/balayya-bot)", # something Unique
    username="balayya-bot",
    password="XXX-YYY-ZZZZ",
)

balayya_slogans = [
  "Coca-Cola Pepsi…Balayya Babu Sexy - Balayya Veera Abhimani",
  "Annam lo Perugu Ledhu Balayya Babu ki Thirugu Ledu - Balayya Veera Abhimani",
  "Palakura Pappu Balayya Babu Nippu - Balayya Veera Abhimani",
  "Vadevadu Videvadu Ma Balayya Babu ki Addu Evadu - Balayya Veera Abhimani",
  "Jill Jill Jiga Maa Balayya Babu sega - Balayya Veera Abhimani",
  "Varshakalam lo Current Kotha Ammaila Gundello Balayya Babu Motha - Balayya Veera Abhimani",
  "Adavilo pudithe simham la puttali Maro janmantuunte balayya abhimanila puttali - Balayya Veera Abhimani",
  "Smoking is injurious – Balayya babu dangerous - Balayya Veera Abhimani",
  "Water quarter – balayya babu dictator - Balayya Veera Abhimani",
]

subs = ["Ni_Bondha", "hyderabad"]

for sub in subs:
  sub_reddit = reddit.subreddit(sub)

  for post in sub_reddit.hot(limit=50):
    for comment in post.comments:
      if ' balayya ' in comment.body.lower():
        random_index = random.randint(0, len(balayya_slogans) - 1)
        comment.reply(balayya_slogans[random_index])
        print("--- Done ---")
        time.sleep(600) # Reddit Bot Limits - Refer: https://www.reddit.com/wiki/bottiquette/ 
