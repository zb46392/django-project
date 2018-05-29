from django import forms

class BookForm(forms.Form):
    naziv = forms.CharField(max_length = 40, required = True, label = 'Naziv')
    autor = forms.CharField(max_length = 40, required = True, label = 'Autor')

class BmiForm(forms.Form):
    weigth = forms.FloatField(min_value=30)
    heigth = forms.FloatField(max_value=2.5)
    CHOICES = [('male','m'), ('female','f')]
    gender = forms.ChoiceField(choices=CHOICES, label='Spol',
        widget=forms.RadioSelect(), initial='male')

    age = forms.IntegerField(min_value=15)
