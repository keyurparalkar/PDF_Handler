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

            return render(request, 'pdfApp/upload_view.html',{'form':form,'data_chunks': UploadData.objects.count()})
    else:
        form = FileUploadform()
        if('data_chunks' in globals()):
            del globals()['data_chunks']
        
        try:
            if(UploadData.objects.count() > 0):
                entries = UploadData.objects.all()
                entries.delete()
                entires.save()
        except:
            print('No PDF records found in database....')

        return render(request, 'pdfApp/upload_view.html',{'form':form})

def file_download(request):
    #Fetch the data from UploadData Table and display it on the console.
    query = UploadData.objects.all()
    print(query)

    #Merge the uploaded pdfs
    MergePDFs()

    pdf = None
    f = open('../test.pdf')
    pdf = File(f)

    # data = ast.literal_eval(json.loads(request.session['data_chunks']))
    data = HttpResponse(pdf, content_type='application/pdf')
    data['Content-Disposition'] = f'filename={timezone.now()}.pdf'
    f.close()

    return data