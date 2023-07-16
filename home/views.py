from django.shortcuts import render
from django.utils.encoding import smart_str
import os.path
from django.shortcuts import redirect,render,HttpResponse
import enc
from django.http import FileResponse, JsonResponse
from home.models import Files

def encrypt(request):
    if request.method=='POST' :
        file=request.FILES["myfile"]
        enc.encryption(file)
    return download1(request)
    
def getkey(request):
  keyinstance= Files.objects.last()
  keyvalue=keyinstance.key
  print("hihihi")
  return HttpResponse(keyvalue)

  

def decrypt(request):
    if request.method=='POST' :
        
        file=request.FILES["myfile"]
        k=request.POST['Key']
        enc.decryption(file,k)
    return download2(request)

def download1(request):
    # Retrieve the latest model instance
    
    latest_file_instance = Files.objects.latest('file')
    
    # Get the file field from the model instance
    file_field = latest_file_instance.file
    
    # Open the file and create a FileResponse
    file_path = file_field.path
    response = FileResponse(open(file_path, 'rb'))
    
    # Set the appropriate content type for the file
    response['Content-Type'] = 'application/octet-stream'
    
    # Set the Content-Disposition header to trigger a file download
    filename = smart_str(file_field.name)  # Ensure filename encoding compatibility
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
    
    return response


def download2(request):
    # Retrieve the latest model instance
    
    latest_file_instance = Files.objects.latest('file')
    
    # Get the file field from the model instance
    file_field = latest_file_instance.file
    
    # Open the file and create a FileResponse
    file_path = file_field.path
    response = FileResponse(open(file_path, 'rb'))
    
    # Set the appropriate content type for the file
    response['Content-Type'] = 'application/octet-stream'
    
    # Set the Content-Disposition header to trigger a file download
    filename = smart_str(file_field.name)  # Ensure filename encoding compatibility
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
    Files.objects.all(). delete ()
    return response

def home(request):
  return  render(request,'index.html')
