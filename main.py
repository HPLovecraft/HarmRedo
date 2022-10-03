import praw

HarmRedoBot = praw.Reddit(username = "user",
                password = "pass",
                client_id = "id",
                client_secret = "scret",
                user_agent = "HarmRedoBot by Flood")

messages = HarmRedoBot.inbox.stream() # makes inbox var
for message in messages: # scan inbox
  try:
    if message in HarmRedoBot.inbox.mentions() and message in HarmRedoBot.inbox.unread(): # If mention | read and unread
        message.reply("hello") # reply with
        message.mark_read() # mark as read
	
  except praw.exceptions.APIException: # If rate limit is reached 
    print("ERROR | API request limit reached...")
