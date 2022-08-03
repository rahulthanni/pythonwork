from Blog.models import users,posts


#print(users)
# username="akhil"
# password="rassword@123"
#
#
#
# user=[user for user in users if user["username"]==username and user["password"]==password]
#
# if user:
#     print("success")
# else:
#     print("failed")
#
#

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session u must login")
    return wrapper


def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

#print(authenticate(username="akhil",password="Password@123"))
session={}
class LoginView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]

        # print(session)


class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        my_post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        print(posts[-1])

class MyPostListView:

    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post


class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postId")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])


log_in=LoginView()
log_in.post(username="richard",password="Password@123")
all_posts=PostListView()
# print(all_posts.get())
#my_post=MyPostListView()
#my_post={"title":"hello good morning","content":"mycontent","liked_by":[]}
#all_posts.post(data=my_post)

like=AddLike()
like.post(postId=1)

# print(my_post.get())
