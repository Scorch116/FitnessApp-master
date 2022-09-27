#Create helper funcitons to communicate with the database
#Cloud data base
#database1-scorchdb116.harperdbcloud.com

#from curses.ascii import TAB
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

#Database Varibles
SCHEMA = "workout_repo"
TABLE = "workouts"
TABLE_TODAY = "workout_today"

#Test dictionary
data = {
    "video_id": "123",
    "title": "Test 1"
}

res = db.insert(SCHEMA, TABLE, [data])
print(res)