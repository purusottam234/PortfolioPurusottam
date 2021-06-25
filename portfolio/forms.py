from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'class': 'form-control  '}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control  ', 'style': 'color: red;'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'class': 'form-control  '}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your Message', 'class': 'form-control  '}))
