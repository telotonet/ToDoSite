from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('email', 'username')
    
    def clean_password2(self,):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2
            
    def clean_email(self,):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise ValidationError('Аккаунт с такой почтой уже зарегистрирован')
        return email
        
    
    def clean_username(self,):
        username = self.cleaned_data.get('username')
        print(username)
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise ValidationError('Имя пользователя существует')
        return username
    
                
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user 