import os
import requests


class GitHubApi:
    def __init__(self):
        self.header = f"Authorization: {os.getenv('GITHUB_ACCESS_TOKEN')}"

    def get_repo(self, owner, repo):
        url = f"https://api.github.com/repos/{owner}/{repo}"
        github_response = requests.get(url, self.header)
        github_response.raise_for_status()
        return github_response.json()
