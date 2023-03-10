from django import forms

class LoginForm(forms.Form):
    userName = forms.CharField(label="User Name", required=True)
    passWord = forms.CharField(widget=forms.PasswordInput())

class CreateUserForm(forms.Form): 
    firstName = forms.CharField(label="First Name", required=True)
    lastName = forms.CharField(label="Last Name", required=True)
    eMail = forms.EmailField(label="E-Mail", required=True)
    passWord = forms.CharField(widget=forms.PasswordInput())
    confirmPassword = forms.CharField(widget=forms.PasswordInput())
    addressLn1 = forms.CharField(max_length=40, label="Address Line 1")
    addressLn2 = forms.CharField(max_length=40, label="Address Line 2")
    city = forms.CharField(max_length=40, label="City")
    zipCode = forms.CharField(max_length=11, label="Zip Code") 

class CreateEventForm(forms.Form):
    date = forms.DateTimeField()
    description = forms.CharField()
    priority = forms.IntegerField()

class CreateThread(forms.Form): 
    pass

class CreateForumnPost(forms.Form): 
    title = forms.CharField(label="Post Title")
    postContent = forms.CharField(label="Post Content")

class createGroup(forms.Form):
    groupName = forms.CharField(label="Group Name", required=True)
    groupDescription = forms.CharField(label="Description of Group", required=True)
    contactInfo = forms.EmailField(label="Email for Contact", required=True)
    meetingTimes = forms.DateTimeField(label="Meeting Time/Date")


