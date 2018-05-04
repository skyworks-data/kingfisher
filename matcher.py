''' matcher.py
    Given the github_final.csv that can be created with fisher.py,
    this script normalizes the data, creates a vector for the given user,
    and matches that user with a nearest-neighbor (NN) match.
    A list of that user's repositories is then returned as potential 
    repositories of interest.
'''

import pandas as pd
from github import Github
import numpy as np
from scipy import spatial
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Import dataset of users with un-normalized row vectors
data = pd.read_csv('github_final.csv', header=None, usecols=range(2,27), skiprows=1)

# Normalize user rows by max
data = data.apply(lambda x: x/x.max(), axis=1)

# Create single column dataframe of usernames
users = pd.read_csv('github_final.csv', header=None, usecols=[1], skiprows=1)

# Collect username to match
username = input("Enter your github username: ")

# Create user vector of the new user
# ENTER USERNAME, PASSWORD
g = Github("jbcampbe", "J3susmy1")

user_vector = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
languages = ['ActionScript', 'C', 'C#', 'C++', 'Clojure', 'CoffeeScript', 'CSS', 'Go', 'Haskell', 'HTML', 'Java', 'JavaScript', 'Lua', 'Matlab', 'Objective-C', 'Perl', 'PHP', 'Python', 'R', 'Ruby', 'Scala', 'Shell', 'Swift', 'TeX', 'Vim script']

user = g.search_users(username)[0]
for repo in user.get_repos():
    for i in range(0, 25):
        if repo.language == languages[i]:
            user_vector[i] += 1

# normalize user vector to match
norm_user_vector = user_vector / max(user_vector)

distance = 1000000
match_index = 0


for i in range(0, len(data)):
    vector = np.array(data.loc[i])
    temp_dist = spatial.distance.cosine(norm_user_vector, vector)

    if temp_dist < distance:
        distance = temp_dist
        match_index = i

matching_user = users.loc[match_index][1]

print("you matched this user:", matching_user)
print("we reccomend these repositories:")
for repo in g.search_users(matching_user)[0].get_repos():
    print(repo.name)