from django import forms

class signUpForm(forms.Form):
    username = forms.CharField(max_length = 100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 100)
    last_name = forms.CharField(max_length = 100)
    contact_number = forms.IntegerField(required = False)
    gender = forms.CharField(max_length = 100, required = False)
    password = forms.CharField(max_length = 100)
    confirm_password = forms.CharField(max_length = 100)

    
class logInForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100)


class blogForm(forms.Form):
    blogTitle = forms.CharField(max_length = 1000)
    blogDescription = forms.CharField(max_length = 2000)
    blogImage = forms.ImageField()
    location = forms.CharField(max_length = 4000, required = False)
    blogContent = forms.CharField(max_length= 50000)

class Search(forms.Form):
	search = forms.CharField(max_length= 200, required=False)

class commentForm(forms.Form):
    comment = forms.CharField(max_length = 5000)