from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Name'
            }))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows':'5',
            'id':'comment',
            'placeholder':'Comment'
        }
    ))
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Author'
            }))