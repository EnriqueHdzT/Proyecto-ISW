from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu Correo'}))
    nombres = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tus Nombres'}))
    apellidoPaterno = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tus Apellido Paterno'}))
    apellidoMaterno = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tus Apellido Materno'}))

    class Meta:
        model = User
        fields = ('username', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingresa tu Nombre de Usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Campo requerido. 150 caracteres o menos. Debe contener letras, digitos y @/./+/-/_ solamente.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingresa tu Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede ser muy similar a tu demas informacion personal.</li><li>Tu contraseña debe tener por lo menos 8 caracteres.</li><li>Tu contraseña no puede ser comun.</li><li>Tu contraseña no puede ser completamente numerica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Valida tu Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que anteriormente para validar esta.</small></span>'