import json
import random
try:
    with open("../Blog/users.json") as f:
        data=json.load(f)
        print(data)

        all_users=[user["id"] for user in data]
        my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
        my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
        to_following=set(all_users)-set(my_followings)
        to_following.remove(my_id)
        print(to_following)
        suggestions=random.sample([*to_following],2)
        print(suggestions)

except Exception as e:

    print(e.__class__)


st=[10,20,30,50,40]
lst={*st}
print(lst)