import praw, random

reddit = praw.Reddit(
    client_id="XXX-YYY-ZZZZ",
    client_secret="XXX-YYY-ZZZZ",
    user_agent="Comment Extraction (by u/balayya-bot)", # something Unique
    username="balayya-bot",
    password="XXX-YYY-ZZZZ",
) # TODO: Reddit App Credentials

comment_header = "> Ignore me, I am a *Safe* **Bot**\n\n"

balayya_slogans = [
  "Coca-Cola Pepsi…Balayya Babu Sexy",
  "Annam lo Perugu Ledhu Balayya Babu ki Thirugu Ledu",
  "Palakura Pappu Balayya Babu Nippu",
  "Vadevadu Videvadu Ma Balayya Babu ki Addu Evadu",
  "Jill Jill Jiga Maa Balayya Babu sega",
  "Varshakalam lo Current Kotha Ammaila Gundello Balayya Babu Motha",
  "Adavilo pudithe simham la puttali Maro janmantuunte balayya abhimanila puttali",
  "Smoking is injurious – Balayya babu dangerous",
  "Water quarter – balayya babu dictator",
]

sub_reddit = reddit.subreddit("#sub_reddit") #TODO: Enter your public Subreddit

for comment in sub_reddit.stream.comments(skip_existing=True):
  if 'balayya' in comment.body.lower() and not comment.author ==  reddit.user.me():
    random_index = random.randint(0, len(balayya_slogans) - 1)
    comment.reply(comment_header + balayya_slogans[random_index])
    print('---- commented on ' + comment.id + ' by ' + comment.author.name + ' ----')
