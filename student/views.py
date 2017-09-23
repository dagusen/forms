from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import StudentForm
from .models import Course, Detail
# Create your views here.

def list_student(request):
	students = Detail.objects.exclude()
	context = {
		'students': students
	}
	return render(request, "index.html", context)
	
class CourseList(View):
	def get(self, request):
		courses = Course.objects.all()
		context = {
			'courses': courses,
		}
		return render(request, "course.html", context)

class StudentDetail(DetailView):
	model = Detail
	template_name = "students.html"
	
	def get_context_data(self, **kwargs):
		context = super(StudentDetail, self).get_context_data(**kwargs)
		return context
		
	
class CourseDetail(DetailView):
	model = Course
	template_name = "course-details.html"
	
	def get_context_data(self, **kwargs):
	
		context = super(CourseDetail, self).get_context_data(**kwargs)
		return context
	

class Student(CreateView):
	def get(self, request):
		student = Detail.objects.all()
		context = {
			'student' : student,
			'form' : StudentForm,
		}
		return render(request, "student-form.html", context)
	
	def post(self, request):
		form = StudentForm(request.POST)
		student = Detail.objects.all()
		
		if form.is_valid():
			form.save()
			return redirect('student')
			
		context = {
			'form' : form,
			'student' : student,
		}
		
		return render(request, "student-form.html", context)

class StudentUpdate(UpdateView):
    model = Detail
    fields = ['first_name', 'last_name', 'middle_name', 'age', 'birthday', 'course']
    template_name = "student-form.html"

class StudentDelete(DeleteView):
    model = Detail
    success_url = reverse_lazy('student')
    template_name = "student-delete-form.html"
