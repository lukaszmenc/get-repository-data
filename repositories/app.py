from flask import Flask
from flask_caching import Cache
from dotenv import load_dotenv
from requests import HTTPError

from repositories.github_client import GitHubApi
from repositories.models import Repository
from repositories.serializers import REPOSITORY_SCHEMA

load_dotenv()

APP = Flask(__name__)
CACHE = Cache(APP, config={"CACHE_TYPE": "simple"})


@APP.route("/repositories/<owner>/<repository>")
@CACHE.cached(timeout=600)
def get_repo(owner, repository):
    github_api = GitHubApi()
    github_repo = github_api.get_repo(owner=owner, repo=repository)
    repo = Repository.from_github_repo(github_repo)
    return REPOSITORY_SCHEMA.dump(repo)


@APP.errorhandler(HTTPError)
def error_handler(error):
    status_code = error.response.status_code

    if status_code == 404:
        return (
            {
                "status": 404,
                "error": "Not Found",
                "message": "requested repository does not exist",
            },
            404,
        )

    return (
        {
            "status": 500,
            "error": "Internal Server Error",
            "message": "the server encountered an unexpected internal server error",
        },
        500,
    )
