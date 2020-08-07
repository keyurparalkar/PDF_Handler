from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from .forms import FileUploadform

# Create your views here.
def file_upload(request):
    if request.method == "POST":
        form = FileUploadform(request.POST, request.FILES)
        if form.is_valid():

            form_data = request.FILES.getlist('file')
            data_chunks = b''
            with open('op.pdf', 'wb+') as f:
                for file in form_data:
                    for data in file.chunks():
                        f.write(data)
                        data_chunks += data
            # data_chunks = HttpResponse(data_chunks, content_type='application/pdf')
            # data_chunks['Content-Disposition'] = 'filename=op_test.pdf'
            
            request.session['data_chunks'] = data_chunks

            return render(request, 'pdfApp/upload_view.html',{'form':form,'data_chunks': data_chunks})
            # return data_chunks
    else:
        form = FileUploadform()
        if('data_chunks' in globals()):
            del globals()['data_chunks']

        return render(request, 'pdfApp/upload_view.html',{'form':form})

def file_download(request):
    data = request.session['data_chunks']
    data = HttpResponse(data, content_type='application/pdf')
    data['Content-Disposition'] = 'filename=op_test.pdf'
    
    return data