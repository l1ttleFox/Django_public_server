from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def upload_file_view(request: HttpRequest) -> HttpResponse:
    context = {
    
    }
    if request.method == "POST" and request.FILES.get("user-file"):
        file = request.FILES["user-file"]
        if file.size < 1048576:
            fs = FileSystemStorage()
            fs.save(file.name, file)
        
        else:
            return render(request, 'requestsapp/file-size-error.html', context=context)
        
    return render(request, 'requestsapp/upload-file.html', context=context)
