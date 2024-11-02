from django import forms
from blog.models import Contact

class ContactForm(forms.ModelForm):
    CIVILITY_CHOISES= (
        ('M.', 'Monsieur'),
        ('Mme.', 'Madame'),
        ('Mlle.', 'Mademoiselle'),
    )
    civility = forms.ChoiceField(choices=CIVILITY_CHOISES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Contact
        fields = ('civility','name', 'email', 'subject', 'message', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'subject': forms.TextInput(attrs={'class' : 'form-control'}),
            'message': forms.Textarea(attrs={'class' : 'form-control'}),
            'file': forms.FileInput(attrs={'class' : 'form-control'}),
        }