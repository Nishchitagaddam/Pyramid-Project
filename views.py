from django.shortcuts import render,redirect
from student.forms import PersonInfoForm
from student.forms import AcademicInfoForm
from student.models import PersonInfo, AcademicInfo
from django.http import HttpResponse

def index(request):
	return HttpResponse("WELCOME TO STUDENT INFORMATION SYSTEM")
	
def base(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)
        if form.is_valid():
            PersonInfo = form.save(commit=False)
            PersonInfo.save()
            return render(request,'app/studentinfo.html',{'form':form})
    else:
        form = PersonInfoForm()
    return render(request, 'app/base.html', {'form': form})
def studentinfo(request):
	#return HttpResponse("Successfully updated")
    if request.method == "POST":
        form = AcademicInfoForm(request.POST)
        if form.is_valid():
            AcademicInfo = form.save(commit=False)
            AcademicInfo.save()
            return render(request,'app/studentinfo.html',{'form':form})
    else:
        form = AcademicInfoForm()
    return render(request, 'app/base.html', {'form': form})
#def success(request):
#    return HttpResponse("Successfully")