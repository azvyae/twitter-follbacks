import app
import sys

try:
    account = sys.argv[1]
except IndexError:
    account = input("Select account: ")

try:
    data = app.loadFiles(account)
    followingList = app.prepareData(data)
    app.printUsers(followingList)
except FileNotFoundError:
    print("Account is not found")
