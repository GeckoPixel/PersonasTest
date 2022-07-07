from django import forms

from .models import Profile

class PostForm(forms.ModelForm):
    CHOICES = ((0, "Masculino"),(1,"Femenino"))
    error_class = 'error-field'
    required_css_class = "required-field"
    name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nombre"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Apellido"}))
    sex = forms.IntegerField(label="Género", widget=forms.RadioSelect(choices=CHOICES))
    birth_date = forms.DateTimeField(label="Fecha de Nacimiento", widget = forms.DateInput(format=('%Y-%m-%d'), attrs={"class":"form-control","type":"date"}))
    class Meta:
        model = Profile
        fields = ('name','last_name','birth_date','sex')