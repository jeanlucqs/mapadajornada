from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Perfil, Habilidade, Competencia, Projeto, Trilha, Carreira

# ========================================================
# 1. MIXIN DE ESTILO (A MÁGICA DO VISUAL)
# ========================================================
# Esta classe deve vir ANTES de qualquer form que a use.
class EstiloFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Verifica se já tem classes para não sobrescrever totalmente
            attrs = field.widget.attrs
            existing_classes = attrs.get('class', '')
            
            # Estilo base para inputs (fundo escuro, borda cinza, foco azul/verde)
            base_style = "w-full bg-gray-900 border border-gray-700 text-white rounded-lg p-3 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all placeholder-gray-600"
            
            if isinstance(field.widget, forms.CheckboxInput):
                attrs['class'] = "w-5 h-5 rounded bg-gray-700 border-gray-600 text-blue-600"
            else:
                attrs['class'] = f"{existing_classes} {base_style}".strip()

# ========================================================
# 2. FORMS DE AUTENTICAÇÃO (LOGIN / REGISTRO)
# ========================================================

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Digite um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilização manual para login/registro
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white focus:border-accent focus:ring-2 focus:ring-accent/50 focus:outline-none transition-colors'
            field.help_text = ''  # Remove textos de ajuda padrão do Django para limpar o visual

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-3 rounded-lg bg-gray-800 border border-gray-700 text-white focus:border-accent focus:ring-2 focus:ring-accent/50 focus:outline-none transition-colors'

# ========================================================
# 3. FORMS DE PERFIL DO USUÁRIO
# ========================================================

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'curso', 'bio']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilização manual para manter consistência
        self.fields['curso'].widget.attrs.update({'class': 'w-full bg-gray-900 border border-gray-700 text-white rounded-xl p-4 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all'})
        self.fields['bio'].widget.attrs.update({'class': 'w-full bg-gray-900 border border-gray-700 text-white rounded-xl p-4 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all resize-none'})

class HabilidadeForm(forms.ModelForm):
    class Meta:
        model = Habilidade
        fields = ['nome']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome']

# ========================================================
# 4. FORM DE PROJETO (ESTILIZADO COM MIXIN)
# ========================================================

class ProjetoForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'link_repositorio', 'link_producao']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ex: E-commerce em React', 'autofocus': True}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva as tecnologias usadas e o objetivo do projeto...'}),
            'link_repositorio': forms.URLInput(attrs={'placeholder': 'https://github.com/seu-usuario/projeto'}),
            'link_producao': forms.URLInput(attrs={'placeholder': 'https://seu-projeto.vercel.app'}),
        }
        labels = {
            'link_repositorio': 'Link do Repositório (GitHub/GitLab)',
            'link_producao': 'Link do Projeto no Ar (Demo/Deploy)',
        }

# ========================================================
# 5. FORMS DO DASHBOARD ADMINISTRATIVO
# ========================================================

class TrilhaForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = Trilha
        fields = ['titulo', 'descricao', 'icone', 'url_nome', 'ordem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'icone': forms.TextInput(attrs={'placeholder': 'Ex: fas fa-code'}),
            'url_nome': forms.TextInput(attrs={'placeholder': 'Ex: trilha_frontend'})
        }

class CarreiraForm(EstiloFormMixin, forms.ModelForm):
    class Meta:
        model = Carreira
        fields = ['titulo', 'categoria', 'descricao', 'url_nome', 'ordem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'url_nome': forms.TextInput(attrs={'placeholder': 'Ex: pagina_front'})
        }