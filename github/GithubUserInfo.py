# Connect to Github and get basic information about user and repositiories
# Author: Harish Chakravarthy
# Licence: MIT

from github import Github
import moment

#Non-authenticated user with no token
USER = 'harishvc'
client = Github()
user = client.get_user(USER)

#Authenticated user
#g = Github("username", "password")
#user = g.get_user()

##### USER INFORMATION
print "Name: %s" % (user.name)
print "Login: %s" % (user.login)
print "#Public  Repos: %s" % (user.public_repos)
print "#Private Repos: %s" % (user.owned_private_repos)
print "Email: %s" % (user.email)
print "Hirable: %s" % (user.hireable)
print "Location: %s" % (user.location)
print "Blog: %s" % (user.blog)
print "Company: %s" % (user.company)
print "Joined on: %s" % (moment.date(user.created_at).format("MMMM DD YYYY"))
print "Last seen on: %s" % (moment.date(user.updated_at).format("MMMM DD YYYY, HH:mm:ss"))

##### PUBLIC REPOSITORY INFORMATION
print "Found ", len(list(user.get_repos())), " repositories for user " , (USER)
print "%-40s %-10s %-10s %-40s" % ("Name", "Private", "Fork", "URL")
for repo in user.get_repos():
    print "%-40s %-10s %-10s %-40s" %  (repo.full_name,repo.private,repo.fork,repo.html_url)
