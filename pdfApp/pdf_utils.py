from .models import UploadData
import PyPDF2
import contextlib

def MergePDFs():
        #Get paths of all the uploaded files.
        paths = [file_obj.upload.path for file_obj in UploadData.objects.all()]    

        #Adding pages to the newly creatred pdf:
        with contextlib.ExitStack() as stack:
            #Create a blank pdf object:
            pdfWriter = PyPDF2.PdfFileWriter()

            files = [stack.enter_context(open(f_path, 'rb')) for f_path in paths]
            for f in files:
                pdfObj = PyPDF2.PdfFileReader(f)
                for page_num in range(pdfObj.numPages):
                    pageObj = pdfObj.getPage(page_num)
                    pdfWriter.addPage(pageObj)
            
            with open('../test.pdf','wb') as f:
                pdfWriter.write(f)

        # for path in paths:
        #     with open(path,'rb') as f:
        #         pdfObj = PyPDF2.PdfFileReader(f)
        #         for page_num in range(pdfObj.numPages):
        #             pageObj = pdfObj.getPage(page_num)
        #             print(f'page obj ======== {pageObj}')
        #             pdfWriter.addPage(pageObj)
        
        # with open('../test.pdf','wb') as f:
        #     pdfWriter.write(f)