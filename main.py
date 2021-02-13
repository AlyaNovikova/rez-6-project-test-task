import sys
import json
import requests


def main(argv):
    if len(argv) != 1:
        print('usage: main.py <repository_link>')
        return
    repos_link = argv[0]

    endpoint = 'https://api.github.com'
    repos = 'repos'
    commits = 'commits'
    owner, repo = repos_link.split('/')[-2:]  # from the repository link, take the owner and repo name

    url = f'{endpoint}/{repos}/{owner}/{repo}/{commits}'
    r = requests.get(url)  # request using GitHub REST API
    commits = json.loads(r.content)

    # Collect all comments to commits and sort them by date
    messages = []
    for commit in commits:
        messages.append((commit['commit']['author']['date'], commit['commit']['message']))
    messages.sort()

    messages = messages[-10:]
    for i, message in enumerate(messages[::-1]):
        print(i, message[1])


if __name__ == "__main__":
    main(sys.argv[1:])
