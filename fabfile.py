from fabric.api import local


# Git deployment setup
def commit():
    """TODO: Docstring for commit.
    :returns: TODO

    """
    local('git add .')
    print("Enter your git commit message: ")
    comment = raw_input()
    local('git commit -m "%s"' % comment)


def prep():
    """TODO: Docstring for prep.
    :returns: TODO

    """
    commit()


def push():
    """TODO: Docstring for deploy.
    :returns: TODO

    """
    local('git push -u origin master')
    local('heroku maintenance:on')
    local('git push heroku master')
    local('heroku maintenance:off')


def deploy():
    """TODO: Docstring for deploy.
    :returns: TODO

    """
    push()
