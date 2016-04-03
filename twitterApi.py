from twython import Twython
twitter = Twython
APP_KEY = '5LpaWBrUl61uhNY9tDPgdgNo6'  # Customer Key here
APP_SECRET = 'r4u9ruzqAwoVosHVjjhydRUAKfHK603LrzxP33U6m5O2h9aUaF'  # Customer secret here
OAUTH_TOKEN = 'Mamama'  # Access Token here
OAUTH_TOKEN_SECRET = 'Papapa'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status="Hello from Python! :D")