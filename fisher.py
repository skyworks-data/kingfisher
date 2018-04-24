from github import Github
import ssl
import pandas as pd

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# using username and password
github = Github('jbcampbe', 'J3susmy1')

# create dataframe
data = pd.DataFrame(columns=['name'])

# Then play with your Github objects:
for user in github.get_users():
    for repo in user.get_repos():
        data.loc[len(data)] = [user.name]
        print(data)