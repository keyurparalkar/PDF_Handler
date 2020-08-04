from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileUploadform

# Create your views here.
def file_upload(request):
    if request.method == "POST":
        form = FileUploadform(request.POST, request.FILES)
        if form.is_valid():
            print(f"Form DATA = {request.FILES['file']}")
            print(f"Form DATA-TYPE = {type(request.FILES['file'])}")

            #trying to opn the file that we recieved in the form of memory:
            form_data = request.FILES['file']
            with open('op.pdf', 'wb+') as f:
                for data in form_data.chunks():
                    f.write(data)

            return HttpResponseRedirect('')
    else:
        form = FileUploadform()
        return render(request, 'pdfApp/upload_view.html',{'form':form})