from django import forms
from .custom_formfields import pdfFileUpload

class FileUploadform(forms.Form):
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,'class': 'browse-ip'}))
    file = pdfFileUpload(label="",widget=forms.ClearableFileInput(
        attrs={'style':'display: none;','accept':'.pdf','multiple': True})
        )