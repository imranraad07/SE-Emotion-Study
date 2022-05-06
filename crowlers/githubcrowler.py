import argparse
import csv
from datetime import datetime

from github import Github
import os

parser = argparse.ArgumentParser()
parser.add_argument('--github_token', type=str, required=True)
parser.add_argument('--type', type=str, required=True, help="pull_request or issue")
parser.add_argument('--repo_name', type=str, required=True)
parser.add_argument('--output_path', type=str, required=True)

args = parser.parse_args()

github_token = args.github_token
type = args.type
repo_name = args.repo_name
output_path = args.output_path

token = os.getenv('GITHUB_TOKEN', github_token)
g = Github(token)
total_count = 5000

repo = g.get_repo(repo_name)
since = datetime.strptime("2020-01-01T00:00:00", "%Y-%m-%dT%H:%M:%S")
# https://github.com/microsoft/TypeScript
with open(output_path, 'w+') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['id', 'created_at', 'user', 'comment'])
    if type == "pull_request":
        issue_comments = repo.get_pulls_comments(direction="desc", sort="updated")
    else:
        issue_comments = repo.get_issue_comments(direction="desc", sort="updated")

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

