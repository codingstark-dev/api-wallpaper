# from bs4 import BeautifulSoup
import requests
import praw
from flask import request, render_template, jsonify
import flask
from flask_restful import Resource, Api, reqparse
from urllib import parse
import time


reddit = praw.Reddit(client_id='W1XGqNQSKF2h4w',
                     client_secret='32CM4A9gSaIGVJFTwCHtKjWt7Xg', password='6b6WNmT*qZQ@qvx',
                     user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36', username='himanshu338')
subreddit = reddit.subreddit('Amoledbackgrounds')
hot_python = subreddit.hot(limit=5)
listfile = []


def redditdatas():
    for submission in hot_python:
        if submission.url.lower().lower().endswith(('.png', '.jpeg', '.jpg')):
            url = requests.head(submission.url, headers={
                                'User-agent': 'your bot 0.1'})
            if url.status_code == 200:
                # print(submission.preview)
                url = submission.url
                filename = submission.title
                listfile.append({
                    "image": url,
                    "title": filename
                })
                time.sleep(1)


                # r = requests.get(url)
                # if r.status_code == 200:
                # if url.endswith(".png"):
                #     with open(filename+'.png', 'wb') as f:
                #         f.write(r.content)
                # elif url.endswith(".jpg"):
                #     with open(filename+'.jpg', 'wb') as f:
                #         f.write(r.content)
                # elif url.endswith(".jpeg"):
                #     with open(filename+'.jpeg', 'wb') as f:
                #         f.write(r.content)


# redditdatas()
# print(len(listfile))
@app.route('/', methods=['GET'])
def home():
    
    return "workingx"


app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.run()
