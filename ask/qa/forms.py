from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate

from .models import Question, Answer, User


class AskForm(ModelForm):
    #author = forms.CharField(disabled=True)

    class Meta:
        model = Question
        fields = ('title', 'text', 'author')
        # Метод save уже определен и сохраняет модель Meta.model


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question', 'author')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.strip() == '':
            raise forms.ValidationError(
                u'Username is empty', code='validation_error')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.strip() == '':
            raise forms.ValidationError(
                u'Email is empty', code='validation_error')
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if password.strip() == '':
            raise forms.ValidationError(
                u'Password is empty', code='validation_error')
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth

