#Create helper funcitons to communicate with the database
#Cloud data base
#database1-scorchdb116.harperdbcloud.com

import harperdb
#URL of cloud DB
url = "https://database1-scorchdb116.harperdbcloud.com"
username = "Admin"
password = "Cooldude00!!"

#Connection to harperDB
db = harperdb.HarperDB(
    url=url,
    username=username,
    password=password
)

print(db.describe_all())