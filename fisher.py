''' fisher.py
    Retrieves data and produces .csv of non-normalized user vectors.
    .csv is preserved at each user iteration for redundancy.
    Actual username and password must be provided on line 22 to retrieve data.
    Script will stop when API limit is reached, and is only for data collection purposes
'''

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
g = Github('jbcampbe', 'J3susmy1')

# create dataframe
data = pd.DataFrame(columns=['name', 'ActionScript', 'C', 'C#', 'C++', 'Clojure', 'CoffeeScript', 'CSS', 'Go', 'Haskell', 'HTML', 'Java', 'JavaScript', 'Lua', 'Matlab', 'Objective-C', 'Perl', 'PHP', 'Python', 'R', 'Ruby', 'Scala', 'Shell', 'Swift', 'TeX', 'Vim script'])

# Then play with your Github objects:
for user in g.get_users():
    userRecord = [user.login, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for repo in user.get_repos():
        for i in range(1, 26):
            if repo.language == data.columns[i]:
                userRecord[i] += 1

    print(userRecord)
    data.loc[len(data)] = (userRecord)
    data.to_csv('github.csv')

data.to_csv = ('github.csv')