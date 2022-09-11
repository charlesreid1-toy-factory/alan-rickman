from github import Github

def fetch():
    k = "ALAN_RICKMAN_GITHUB_ACCESS_TOKEN"
    if k not in os.environ:
        err = "Error: could not proceed because no {k} environment variable defined."
        err += " Try running 'source environment' in the repository root."
        raise Exception(err)

    # create Github instance using access token
    g = Github(os.environ[k])
    repo = g.get_repo("charlesreid1/five-letter-words")
    return repo.git_url
