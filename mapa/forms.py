from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil, Habilidade, Competencia, Projeto

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


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'curso',]

class HabilidadeForm(forms.ModelForm):
    class Meta:
        model = Habilidade
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full','placeholder':'Ex: Raciocínio lógico'})
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'border rounded-lg p-2 w-full','placeholder':'Ex: Python'})
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'link_repositorio', 'link_producao']
        
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Nome do Projeto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Descreva seu projeto...', 'rows': 4
            }),
            'link_repositorio': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'https://github.com/seu-usuario/seu-projeto'
            }),
            'link_producao': forms.URLInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'https://meu-projeto.com'
            }),
        }
        labels = {
            'titulo': 'Título do Projeto',
            'descricao': 'Descrição',
            'link_repositorio': 'Link do Repositório',
            'link_producao': 'Link da Aplicação (Online)',
        }
        