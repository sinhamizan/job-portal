from django.contrib import admin
from .models import Recruiter_Register, Job_Seeker_Register, Category, Job_Post, Job_Apply, Blog_Post, NotificationForRecruiter, Create_Interview, Interview_Notification, Create_CV_Academic_Qualification, Create_CV_Add_Referance, Create_CV_Basic_info, Create_CV_Job_Experience, Create_CV_Language_Profiency, Create_CV_Traning, Create_CV_Skill, Create_CV_Signiture, Create_CV_Hobby, Create_CV_Career_Objective, Create_CV_Picture

# Register your models here.
@admin.register(Recruiter_Register)
class Recruiter_RegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']

@admin.register(Job_Seeker_Register)
class Job_Seeker_Register_admin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']

admin.site.register(Category)

class Job_Post_admin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'posted_date']
admin.site.register(Job_Post, Job_Post_admin)

# class Job_Apply_admin(admin.ModelAdmin):
#     list_display = ['phone_No']
admin.site.register(Job_Apply)

@admin.register(Blog_Post)
class Blog_Post_admin(admin.ModelAdmin):
    list_display = ['title', 'post_at']

admin.site.register(NotificationForRecruiter)
admin.site.register(Create_Interview)

class Interview_Notification_admin(admin.ModelAdmin):
    list_display = ['title', 'is_view', 'date']
admin.site.register(Interview_Notification, Interview_Notification_admin)

admin.site.register(Create_CV_Academic_Qualification)
admin.site.register(Create_CV_Add_Referance)
admin.site.register(Create_CV_Basic_info)
admin.site.register(Create_CV_Job_Experience)
admin.site.register(Create_CV_Language_Profiency)
admin.site.register(Create_CV_Traning)
admin.site.register(Create_CV_Skill)
admin.site.register(Create_CV_Signiture)
admin.site.register(Create_CV_Career_Objective)
admin.site.register(Create_CV_Hobby)
admin.site.register(Create_CV_Picture)