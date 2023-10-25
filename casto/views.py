from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import UploadFileForm
import openpyxl

# from somewhere import handle_uploaded_file

def handle_uploaded_file():
    pass
    # with open("some/file/name.txt", "wb+") as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)

def index(request):
    template = loader.get_template('casto_templates/index.html')
    return render(request, 'casto_templates/index.html')


def upload_file(request):
    if "GET" == request.method:
        return render(request, 'casto_templates/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()

        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
                print(row_data)
            excel_data.append(row_data)




        return render(request, 'casto_templates/index.html', {"excel_data":excel_data})