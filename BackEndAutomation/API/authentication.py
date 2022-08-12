import requests
from Utilities.configurations import *

url = "https://github.com/login"
github_res = requests.get(url, auth=('apparaojaji@gmail.com', getPassword()))
print(github_res.status_code)

# Another way, via Session Manager
se = requests.session()
se.auth = auth=('apparaojaji@gmail.com', getPassword())
github_res2 = se.get(url)
print(github_res2.status_code)


