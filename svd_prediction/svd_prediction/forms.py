from django import forms

class SVDPredictionForm(forms.Form):
    user_id = forms.IntegerField(label="", widget=forms.TextInput({'placeholder': 'User ID'}))
    #movie_id = forms.IntegerField(label="", widget=forms.TextInput({'placeholder': 'Movie ID'}))
