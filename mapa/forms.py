from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'Email'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = "Nome de Usuário"
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Nome de Usuário', 'autofocus': True}
        )
        
        self.fields['password1'].label = "Senha"
        self.fields['password1'].widget.attrs.update({'placeholder': 'Senha'})
        
        self.fields['password2'].label = "Confirme a Senha"
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirme a Senha'})
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Nome de Usuário', 'autofocus': True}
        )
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Senha'}
        )