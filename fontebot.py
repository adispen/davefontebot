import time
import praw

user_agent = ("davefontebot/1.0 by orangesodasmurf"
			  "replies to comments about hackathons"
			  "by saying Hell Yeah! like Dave himself"
			  "github.com/adispen/davefontebot")
r = praw.Reddit(user_agent = user_agent)

r.login('DaveFonteBot', 'HellYeah')
subreddit = r.get_subreddit('114g')
subreddit_comments = subreddit.get_comments()
already_done = set()

buzzWords = ['hackathon', 'hackathons', 'mhacks', 'hackru', 'pennapps', 'hackmit', 'hackny']
while True:
	for comment in subreddit_comments:
		comment_text = comment.body.lower()
		has_buzz = any(string in comment_text for string in buzzWords)
		if comment.id not in already_done and has_buzz:
			comment.reply("Helllllll yeah!")
			already_done.add(comment.id)
	time.sleep(300)
