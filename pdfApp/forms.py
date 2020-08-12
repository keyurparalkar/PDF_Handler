from django import forms

class FileUploadform(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class': 'browse-ip'}))