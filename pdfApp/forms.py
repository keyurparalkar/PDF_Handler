from django import forms
from .custom_formfields import pdfFileUpload

class FileUploadform(forms.Form):
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class': 'browse-ip'}))
    file = pdfFileUpload(widget=forms.ClearableFileInput(attrs={'multiple': True,'class': 'browse-ip'}))