from django.conf.urls import url
from student import views
app_name = 'student'
urlpatterns = [ 
	url(r'^$',views.index,name = 'index'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^studentinfo$',views.studentinfo,name = 'studentinfo'),
	#url(r'^success$',views.success,name = 'success'),
	
	
]