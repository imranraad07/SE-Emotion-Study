import csv
import json
import time
from datetime import datetime

from github import Github
import os

token = os.getenv('GITHUB_TOKEN', '...')
g = Github(token)
total_count = 5000
repo = g.get_repo("webpack/webpack")

since = datetime.strptime("2020-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
# https://github.com/microsoft/TypeScript
with open('../dataset/github/pull_requests/webpack.csv', 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['id', 'created_at', 'user', 'comment'])
    issue_comments = repo.get_pulls_comments(direction="desc", sort="updated")
    print(issue_comments.totalCount)

    count = 0
    for idx in range(0, issue_comments.totalCount):
        if count > total_count:
            break
        try:
            print(idx, count)
            for comment in issue_comments.get_page(idx):
                try:
                    if '-bot' in comment.user.login or 'bot-' in comment.user.login:
                        continue
                    print(comment.created_at)
                    csvwriter.writerow([comment.id, comment.created_at, comment.user.login, comment.body])
                    count = count + 1
                except:
                    print("Exception occurred")
        except:
            print("Exception occurred in rest request")
