from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import FileUploadform

# Create your views here.
def file_upload(request):
    if request.method == "POST":
        form = FileUploadform(request.POST, request.FILES)
        if form.is_valid():

            form_data = request.FILES.getlist('file')

            with open('op.pdf', 'wb+') as f:
                for file in form_data:
                    for data in file.chunks():
                        f.write(data)

            return HttpResponseRedirect('')
    else:
        form = FileUploadform()
        return render(request, 'pdfApp/upload_view.html',{'form':form})

#Class to handle multiple file uploads:
# class file_upload(FormView):
#     form_class = FileUploadform
#     template_name = 'pdfApp/upload_view.html'
#     success_url = ''

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 print(f)
#                 return self.form_valid(form)
#         else:
#             return self.form_invalid(form)