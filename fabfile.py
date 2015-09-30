from fabric.api import local


# Git deployment setup
def deploy():
    """TODO: Docstring for deploy.
    :returns: TODO

    """
    local("git add .")
    print("Enter your git commit comment: ")
    comment = raw_input()
    local('git commit -m "%s"' % comment)
    local('git push -u origin master')
    local('heroku maintenance:on')
    local('git push heroku master')
    local('heroku maintenance:off')
