from django import forms 

class Contacto(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Inserte su nombre'}), required=True)
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Inserte su email'}), max_length=100, required=True)
    asunto=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Inserte el asunto'}), max_length=100, required=True)
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Inserte el mensaje','cols':3,'rows':5}), required=True)