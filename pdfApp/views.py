from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.utils import timezone
from .forms import FileUploadform
from .models import UploadData
from .pdf_utils import MergePDFs
import json
import ast


# Create your views here.
def file_upload(request):
    if request.method == "POST":
        form = FileUploadform(request.POST, request.FILES)
        if form.is_valid():
            form_data = request.FILES.getlist('file')

            for file_data in form_data:
                instance = UploadData(upload=file_data)
                instance.save()
            
            return render(request, 'pdfApp/upload_view.html',{'form':form,'fnames_pk': UploadData.objects.all()})
    else:
        form = FileUploadform()
        print("FILE ID = ",request.GET.get('file_id'))
        if(request.GET.get('file_id') != None):
            file_id = request.GET.get("file_id")
            file_op = UploadData.objects.get(pk=file_id)
            file_op.delete()
            file_op.save()
        else:
            try: #fix the below lines of code: on refresh page.
                if(UploadData.objects.count() > 0):
                    entries = UploadData.objects.all()
                    entries.delete()
                    entires.save()
            except:
                print("Data Not found .....")

        

        return render(request, 'pdfApp/upload_view.html',{'form':form, 'fnames_pk':False })

def file_download(request):
    #Fetch the data from UploadData Table and display it on the console.
    query = UploadData.objects.all()
    print(query)

    #Merge the uploaded pdfs
    MergePDFs()

    pdf = None
    f = open('../test.pdf','rb')
    pdf = f.read()

    data = HttpResponse(pdf, content_type='application/pdf')
    data['Content-Disposition'] = f'filename={timezone.now()}.pdf'
    f.close()

    return data


def remove_upload(request,pk):
    print(f"File ID = {pk}")
    print(request)
    return render(request,'pdfApp/upload_view.html')