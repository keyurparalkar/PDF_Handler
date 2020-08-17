from django import forms
from django.core.exceptions import ValidationError
import magic
import sys

class pdfFileUpload(forms.FileField):
    def to_python(self, value):
        return value

    def validate(self, value):
        #get the mime type from the buffer:
        mime_type = magic.from_buffer(value.file.getvalue(), mime=True)

        #check if the mime type matches with mime type of pdf
        if('application/pdf' not in mime_type):
            raise ValidationError('Unsupported File Type ..', code='unsupported_ftype')

        #check if the combined upload file sizes should be less than 25 MB
        print(f"total uploaded file size == {sys.getsizeof(value.file.getvalue())}")
        total_file_size = sys.getsizeof(value.file.getvalue())
        if(total_file_size >  2.5e7):
            raise ValidationError("Total file size should be less that 2 MB", code="filesize_limit_exceed")