import pymysql.cursors
db = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='contact-app-flask'
)

cursor = db.cursor()

nama = "Yukie Muhammad Billal"

from . import contact