from django.shortcuts import render
from .forms import FileUploadform

# Create your views here.
def file_upload(request):
    form = FileUploadform()
    return render(request, 'pdfApp/upload_view.html',{'form':form})