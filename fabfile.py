from fabric.api import local


# Git deployment setup
def commit():
    """TODO: Docstring for commit.
    :returns: TODO

    """
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -m '{}'".format(message))


def push():
    """TODO: Docstring for push.
    :returns: TODO
    push to GitHub

    """
    local("git push origin master")


def prepare():
    """TODO: Docstring for prepare.
    :returns: TODO

    """
    push()