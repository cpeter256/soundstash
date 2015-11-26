from django import forms

class userForm(forms.Form):
	usr = forms.CharField(label='Desired Username', max_length=200)
	usr_email = forms.EmailField(label='Email', max_length=200)
	usr_first = forms.CharField(label='First Name (optional)', max_length=200)
	usr_last = forms.CharField(label='Last Name (optional)', max_length=200)
	usr_pwd = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)
	usr_pwd1 = forms.CharField(label='Reenter Password', max_length=200, widget=forms.PasswordInput)

