from django.contrib import admin
from .models import Detail, Course, Subject, professor

#@admin.register(Details)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ("course_name", "description", )
	list_editable = ("description",)
	list_filter = ("course_name", )
	search_fields = ("course_name",  )

admin.site.register(Detail)
#admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
#admin.site.register(professor)

# Register your models here.
