

from authentication.models import users



def authenticate(**kwargs):
    uname=kwargs.get("username")
    pwd=kwargs.get("password")
    user=[ for user in users if user["username"]=uname and ]
    print(users)

authenticate(username="django",password="django@123") 
