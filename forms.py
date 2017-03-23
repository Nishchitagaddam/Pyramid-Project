from django.forms import ModelForm
from student.models import PersonInfo, AcademicInfo,AdditionalInfo,Notifications

class PersonInfoForm(ModelForm):
	class Meta:
		model = PersonInfo
		fields = '__all__'
		
class AcademicInfoForm(ModelForm):
	class Meta:
		model = AcademicInfo
		fields = '__all__'
				