from TikTokApi import TikTokApi
api = TikTokApi()
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# bot config
username = config['pyTikfollower']['username']

def on_new_follow():
    print('New follower!')

while True:
    user = api.getUser(username=username)
    currentct = user['userInfo']['stats']['followerCount']
    print(f'You are currently at {currentct} followers')
    with open('lastct.txt', 'r') as f:
        lastcount = int(f.read())
    if lastcount < currentct:
        with open('lastct.txt', 'w') as f:
            f.write(str(currentct))
        on_new_follow()
    sleep(5)
