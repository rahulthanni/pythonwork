import json

with open("blogs.json",encoding="utf-8") as f:
    data=json.load(f)
    print(data)


print(len(data))

#number of post by userId=1

num_post=[post for post in data if post["userId"]==1]
print(len(num_post))

#total number of likes for postId 6
like_post=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(like_post)

#nummber of post liked by user=2
post_liked=len([post for post in data if 2 in post["liked_by"]])
print(post_liked)
