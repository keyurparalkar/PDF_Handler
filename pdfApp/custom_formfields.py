from django import forms
from django.core.exceptions import ValidationError
import magic

class pdfFileUpload(forms.FileField):
    def to_python(self, value):
        return value

    def validate(self, value):
        #get the mime type from the buffer:
        print(f"Value in VALIDATE ===== {value.file}")
        mime_type = magic.from_buffer(value.file.getvalue(), mime=True)
        print(f"mime-Type ===== {mime_type}")
        if('application/pdf' not in mime_type):
            raise ValidationError('Unsupported File Type ..')
        



