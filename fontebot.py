import time
import praw
import os

PASSWORD = os.environ.get('BOTPASS')

user_agent = ("davefontebot/1.0 by orangesodasmurf"
			  "replies to comments about hackathons"
			  "by saying Hell Yeah! like Dave himself"
			  "github.com/adispen/davefontebot")
r = praw.Reddit(user_agent = user_agent)

r.login('DaveFonteBot', PASSWORD)
subreddit = r.get_subreddit('114g+ahf4')
already_done = set()
x = 1

buzzWords = ['hackathon', 'hackathons', 'mhacks', 'hackru', 'pennapps', 'hackmit', 'hackny']
while True:
	subreddit_comments = subreddit.get_comments()
	for comment in subreddit_comments:
		comment_text = comment.body.lower()
		has_buzz = any(string in comment_text for string in buzzWords)
		x += 1
		if comment.id not in already_done and has_buzz:
			print comment.author
			print comment.body
			print comment.id
			print x
			#comment.reply("Helllllll yeah!")
			already_done.add(comment.id)
	print x
	time.sleep(2)
