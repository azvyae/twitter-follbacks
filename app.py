import json
import os
import yaml


def convertJsToJson(file, account):
    checkWords = (f'window.YTD.{file}.part0 =',
                  f'{file}:', "accountId", "userLink", ";")
    repWords = ("", f'"{file}":', '"accountId"',
                '"userLink"', '')

    fin = open(f"./accounts/{account}/{file}.js", "rt")
    fout = open(f"./accounts/{account}/{file}.json", "wt")
    for line in fin:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        fout.write(line)
    fin.close()
    fout.close()

    data = yaml.safe_load(open(f"./accounts/{account}/{file}.json"))
    data = json.dumps(data)

    with open(f"./accounts/{account}/{file}.json", "w") as outfile:
        outfile.write(data)
    os.remove(f"./accounts/{account}/{file}.js")


def loadFiles(account):
    data = {}
    try:
        convertJsToJson('follower', account)
        convertJsToJson('following', account)
    except FileNotFoundError:
        pass

    with open(f"./accounts/{account}/follower.json") as file:
        data["followers_json"] = json.load(file)

    with open(f"./accounts/{account}/following.json") as file:
        data["following_json"] = json.load(file)

    try:
        with open(f"./accounts/{account}/exclude.json") as file:
            data["excluded_json"] = json.load(file)
    except FileNotFoundError:
        print("Continuing without excluded accounts")

    try:
        with open(f"./accounts/{account}/unfollowed.json") as file:
            data["unfollowed_json"] = json.load(file)
    except FileNotFoundError:
        print("Continuing without unfollowed accounts")

    return data


def prepareData(data):
    followingList = []
    for following in data["following_json"]:
        followingList.append(following["following"]["userLink"])

    for follower in data["followers_json"]:
        if follower["follower"]["userLink"] in followingList:
            followingList.remove(follower["follower"]["userLink"])

    if data.get("excluded_json") != None:
        for exclude in data["excluded_json"]["excluded"]:
            if exclude in followingList:
                followingList.remove(exclude)
    if data.get("unfollowed_json") != None:
        for unfollowed in data["unfollowed_json"]["unfollowed"]:
            if unfollowed in followingList:
                followingList.remove(unfollowed)

    return followingList


def printUsers(followingList):
    if len(followingList) > 0:
        for user in followingList:
            print(user)
    else:
        print("There are no users you follow but don't follow back")
