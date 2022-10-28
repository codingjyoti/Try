from webbrowser import get
from django.shortcuts import render, redirect
from django.urls import is_valid_path  
from .models import Student
from  .forms import Studentform
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def student(request):
    if request.method == "POST":
        form=Studentform(request.POST)   

        if form.is_valid():
            
           try:
                form.save()
                return redirect("/")
           except Exception as e:
               print(e)
    else:
        form= Studentform()
    return render(request,'index.html',{'form':form})

def show(request):  
    students=Student.objects.all().order_by('-id') 
    paginator = Paginator(students,5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
     
    return render(request,"show.html",{'students':page_obj})

def edit(request,id):

    student = Student.objects.get(id=id)
    return render(request,"edit.html",{'student':Student}) 

def update(request,id):
    print(id)
    if request.method == "POST":
        print(id)
        student = get_object_or_404(Student, pk=id)
        form = Studentform(request.POST, instance=student)
        if form.is_valid():  
            form.save()  
            return redirect("/")
        
    else:
        student = get_object_or_404(Student, pk=id)
        return render(request,'edit.html',{'student':student})


def destroy(request, id):  
    print(id)
    student= Student.objects.get(id=id)  
    print(student)
    student.delete()  
    return redirect("/")


def delete_form(request):
    if request.method == 'GET':
        return render(request, 'delete-form.html')

    
    else:
        s_id = request.POST.get('s_id')

        student = Student.objects.get(id=s_id)
        student.delete()

        return redirect("/show")





