from django import forms

class BookForm(forms.Form):
    naziv = forms.CharField(max_length = 40, required = True, label = 'Naziv')
    autor = forms.CharField(max_length = 40, required = True, label = 'Autor')
