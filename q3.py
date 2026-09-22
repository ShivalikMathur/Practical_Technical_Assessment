import json

def getscore(user):
    return user["score"]

with open("users.json") as file:
    users = json.load(file)

unique_users = {}

for user in users:
    if user["score"] >= 50:
        unique_users[user["user_id"]] = user

users = list(unique_users.values())
scores = [user["score"] for user in users]

result = {
    "average_score": sum(scores) / len(scores),
    "maximum_score": max(scores),
    "minimum_score": min(scores),
    "top_10_users": sorted(users, key=getscore, reverse=True)[:10]
}

print(json.dumps(result))