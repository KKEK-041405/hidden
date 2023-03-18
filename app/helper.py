from django.contrib.auth.models import User,Group
def CreateUser(Cleaned_data):
        if CheckUserExistence(Username = Cleaned_data["pinno"] ):
            newUser = User(username=Cleaned_data["pinno"],is_superuser=False)
            newUser.set_password(Cleaned_data["password"])
            newUser.save()
            studentgroup = Group.objects.get(name="Students")
            studentgroup.user_set.add(newUser)
            return True
        return False

def CheckUserExistence(Username):
    if(not User.objects.filter(username=Username).exists()):
        return True
    else:
        return False
    
