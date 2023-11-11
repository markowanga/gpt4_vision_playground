from pathlib import Path

import git
from dotenv import dotenv_values


def get_openai_key() -> str:
    get_env_variables()['']


def get_git_root(path: Path = Path('.')) -> Path:
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return Path(git_root)


def get_env_variables():
    return dotenv_values(get_git_root() / ".env")
