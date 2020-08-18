from marshmallow import utils


class Repository:
    def __init__(self, fullName, description, cloneUrl, stars, createdAt):
        self.fullName = fullName
        self.description = description
        self.cloneUrl = cloneUrl
        self.stars = stars
        self.createdAt = utils.from_iso_datetime(createdAt)

    @staticmethod
    def from_github_repo(github_repo):
        return Repository(
            github_repo["full_name"],
            github_repo["description"],
            github_repo["clone_url"],
            github_repo["stargazers_count"],
            github_repo["created_at"],
        )
