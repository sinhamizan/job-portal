from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Recruiter_Register, Job_Seeker_Register, Job_Post, Category, Blog_Post, Job_Apply, NotificationForRecruiter, Create_Interview, Interview_Notification, Create_CV_Basic_info, Create_CV_Hobby, Create_CV_Career_Objective, Create_CV_Skill, Create_CV_Signiture, Create_CV_Add_Referance, Create_CV_Academic_Qualification, Create_CV_Language_Profiency, Create_CV_Picture, Create_CV_Traning, Create_CV_Job_Experience

from django.contrib import messages
from .forms import new_job_form, Job_Seeker_Register_Form, Recruiter_Register_Form, Job_Apply_Form, CV_Basic_Info_Form, Create_CV_Academic_Form, Create_CV_Traning_Form, Create_CV_Job_Experience_Form, Create_CV_Add_Referance_Form
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator
import datetime

# Create your views here.

def Home(request):
    cat = Category.objects.all()
    #for todays job 
    jobs = Job_Post.objects.all()
    today_job = jobs.filter(posted_date=date.today())
    #Government Jobs
    govt_jobs = jobs.filter(category='5')
    # POST
    posts = Blog_Post.objects.all()[:4]
   
    context = {
        'cat':cat,
        'govt_jobs':govt_jobs,
        'total_govt_jobs':govt_jobs.count(),
        'today_job':today_job,
        'total_today_job':today_job.count(),
        'posts':posts,
        'jobs':jobs,
    }
    return render(request, 'home.html', context)


def do_registration(request):
    return render(request, 'do_registration.html')


def do_login(request):
    return render(request, 'do_login.html')


def recruiter_register(request):
    form = Recruiter_Register_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.info(request, "Your are Successfully Registered.")
        return redirect('jobapp:do_login') 
    
    context = {
        'form':form,
    }
    return render(request, 'recruiter/recruiter_register.html', context)


def job_seeker_register(request):
    if request.method == 'POST':
        form = Job_Seeker_Register_Form(request.POST or None, request.FILES)
        if form:
            instance = form.save(commit=False)
            instance.save()
            messages.info(request, "Your are Successfully Registered.")
            return redirect('jobapp:do_login')
    else:
        form = Job_Seeker_Register_Form()

    context = {
        'form':form,
    }
    template = 'jobseeker/job_seeker_register.html'
    return render(request, template, context)

def recruiter_login(request):
    # if request.session['recruiter_id']:
    #     return redirect('jobapp:home')
    # else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth = Recruiter_Register.objects.filter(username=username, password=password).first()

        if auth:
            request.session['recruiter_id'] = auth.id
            request.session['recruiter_name'] = auth.username
            messages.info(request, "Your are Successfully Login.")
            return redirect('jobapp:home')
        else:
            messages.warning(request, "Invalid Username or Password !")
            return render(request, 'recruiter/recruiter_login.html')
    return render(request, 'recruiter/recruiter_login.html')


def job_seeker_login(request):
    # if request.session['job_seeker_id']:
    #     return redirect('jobapp:home')
    # else:
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth = Job_Seeker_Register.objects.filter(username=username, password=password).first()

        if auth:
            request.session['job_seeker_id'] = auth.id
            request.session['job_seeker_name'] = auth.username
            messages.info(request, "Your are Successfully Login.")
            return redirect('jobapp:home')
        else:
            messages.warning(request, "Invalid Username or Password !")
            return render(request, 'jobseeker/job_seeker_login.html')
            
    return render(request, 'jobseeker/job_seeker_login.html')



def  recruiter_logout(request):
    request.session['recruiter_id'] = None
    request.session['recruiter_name'] = None
    return redirect('jobapp:do_login')


def  job_seeker_logout(request):
    request.session['job_seeker_id'] = None
    request.session['job_seeker_name'] = None
    return redirect('jobapp:do_login')

def all_job(request):
    job = Job_Post.objects.all().order_by('-posted_time')
    category = Category.objects.all()

    # pagination
    per_page = Paginator(job, 5)
    page_num = request.GET.get('page')
    page_obj = per_page.get_page(page_num)

    context = {
        'job':page_obj,
        'total_job':job.count(),
        'category':category,
    }
    return render(request, 'all_job.html', context)


def job_detail(request, id):
    job = get_object_or_404(Job_Post, id=id)

    context = {
        'job':job,
    }
    return render(request, 'job_detial.html', context)


def recruiter_profile(request, name):
    recruiter = get_object_or_404(Recruiter_Register, username = name)
    job = Job_Post.objects.filter(recruiter = recruiter.id)

    context = {
        'recruiter':recruiter,
        'job':job,
        'total_job':job.count()
    }
    return render(request, 'recruiter/recruiter_profile.html', context)


def update_recruiter_profile(request, name):
    recruiter = get_object_or_404(Recruiter_Register, username = name)
    
    form = Recruiter_Register_Form(request.POST or None, request.FILES or None, instance=recruiter)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.info(request, "Your are Successfully Updated Profile.")
        return redirect('jobapp:recruiter_profile', name=request.session['recruiter_name']) 

    context = {
        'form':form,
    }
    template = 'recruiter/update_recruiter_profile.html'
    return render(request, template, context)


def job_seeker_profile(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username = name)

    context = {
        'job_seeker':job_seeker,
    }
    return render(request, 'jobseeker/job_seeker_profile.html', context)


def update_job_seeker_profile(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username = name)

    context = {
        'job_seeker':job_seeker,
    }
    template = 'jobseeker/update_job_seeker_profile.html'
    return render(request, template, context)


def post_job(request):
    recruiter = get_object_or_404(Recruiter_Register, username=request.session['recruiter_name'])
    new_job = new_job_form(request.POST or None)
    if new_job.is_valid():
        instance = new_job.save(commit=False)
        instance.recruiter=recruiter
        instance.save()
        messages.info(request, "Post a New Job Successfully.")
        return redirect('jobapp:all_job')

    context = {
        'new_job':new_job,
    }
    return render(request, 'recruiter/post_job.html', context)


def edit_job(request, id):
    data = get_object_or_404(Job_Post, id=id)
    new_job = new_job_form(request.POST or None, instance=data)
    if new_job.is_valid():
        instance = new_job.save(commit=False)
        instance.save()
        messages.info(request, "Job Successfully Updated.")
        return redirect('jobapp:home')

    context = {
        'new_job':new_job,
    }
    return render(request, 'recruiter/edit_job.html', context)


def delete_job(request, id):
    data = get_object_or_404(Job_Post, id=id)
    data.delete()
    messages.info(request, "Job was Delete.")
    return redirect('jobapp:home')


def apply_job(request, id):
    job = get_object_or_404(Job_Post, id=id)
    job_seeker = get_object_or_404(Job_Seeker_Register, id=request.session['job_seeker_id'])
    recruiter = get_object_or_404(Recruiter_Register, id=job.recruiter_id)

    form = Job_Apply_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.job = job
        form.recruiter = recruiter
        form.job_seeker = job_seeker
        form.save()

        ntc_title = "You received a new application for {} ".format(job.title)
        ntc_des = """
            <p>Application From</p> 
            Full Name: {} 
            Email: {} 
            Phone No.: {} 
            CV: {} 
        """.format(job_seeker.full_name, job_seeker.email, form.phone_No, form.cv)
        NotificationForRecruiter.objects.create(recruiter_id=recruiter.id, title=ntc_title, description=ntc_des)
        return redirect('jobapp:welcome_message')
        
    return render(request, 'jobseeker/apply_job.html', {'form':form})


def application_list(request, name):
    #applicator = get_object_or_404(Job_Apply, job_seeker_email=name)
    application_lists = Job_Apply.objects.all()

    context = {
        'application_lists':application_lists,
        'total_application':application_lists.count(),
    }
    template = 'jobseeker/application_list.html'
    return render(request, template, context)

def recruiter_posted_job(request, name):
    recruiter = get_object_or_404(Recruiter_Register, username = name)
    job = Job_Post.objects.filter(recruiter = recruiter.id)

    context = {
        'recruiter':recruiter,
        'job':job,
        'total_job':job.count()
    }
    return render(request, 'recruiter/recruiter_posted_job.html', context)


def todays_job(request):
    today_job = Job_Post.objects.filter(posted_date=date.today())

    context = {
        'today_job':today_job,
        'total_today_job':today_job.count(),
    }
    return render(request, 'todays_job.html', context)


def category_wise(request, name):
    cate = get_object_or_404(Category, name=name)
    cat_wise_job = Job_Post.objects.filter(category=cate.id)

    context = {
        'cate':cate,
        'cat_wise_job':cat_wise_job,
        'total_this_cat_job':cat_wise_job.count(),

    }
    return render(request, 'category_wise.html', context)


def company_wise(request, name):
    user = get_object_or_404(Recruiter_Register, username=name)
    company_wise_job = Job_Post.objects.filter(recruiter=user.id)

    context = {
        'company':user,
        'company_wise_job':company_wise_job,
        'total_this_company_job':company_wise_job.count(),

    }
    return render(request, 'company_wise_job.html', context)

def job_search_page(request):
    job = Job_Post.objects.all()
    searched_data = request.GET.get('q')
    if searched_data:
        job = job.filter(
            Q(title__icontains=searched_data)
        )
    else:
        return redirect('jobapp:job_search_page')

    context = {
        'job':job,
        'searched_data':searched_data,
        'total_searched_job':job.count(),
    }
    return render(request, 'job_search_page.html', context)

def blog_posts(request):
    posts = Blog_Post.objects.all()

    context = {
        'posts':posts,
    }
    template = 'blog_post.html'
    return render(request, template, context)


def single_post(request, id):
    blog = get_object_or_404(Blog_Post, id=id)

    context = {
        'blog':blog,
    }
    template = 'single_post.html'
    return render(request, template, context)

def error_message(request):
    return render(request, 'error_message.html')

def welcome_message(request):
    return render(request, 'welcome_message.html')


def jobseeker_change_password(request, name):
    jobseeker = Job_Seeker_Register.objects.get(username=name)
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if jobseeker.password == old_password:
            if new_password == confirm_password:
                jobseeker.password = new_password
                jobseeker.save()
                messages.success(request,"Password Updated Successfully")  
                request.session['job_seeker_id'] = None
                request.session['job_seeker_name'] = None
                return redirect('jobapp:job_seeker_login')
            else: 
                messages.error(request,"Password doesn't Matched")
        else:
            messages.error(request,"Old Password doesn't Matched")

    template = 'jobseeker/job_seeker_change_password.html'
    return render(request, template)


def recruiter_change_password(request, name):
    recruiter = Recruiter_Register.objects.get(username=name)
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if recruiter.password == old_password:
            if new_password == confirm_password:
                recruiter.password = new_password
                recruiter.save()
                messages.info(request, "Password Updated Successfully.")
                request.session['recruiter_id'] = None
                request.session['recruiter_name'] = None
                return redirect('jobapp:recruiter_login')
            else:
                messages.warning(request, "Password Doesn't Matched.")
        else:
            messages.warning(request, "Old Password Doesn't Matched.")
    template = 'recruiter/recruiter_change_password.html'
    return render(request, template)


def recruiter_notification(request, name):
    recruiter = Recruiter_Register.objects.get(username=name)

    notification = NotificationForRecruiter.objects.filter(recruiter=recruiter).order_by('-date')

    context = {
        'notification':notification,
        'total_notification':notification.count(),
    }
    template = 'recruiter/recruiter_notification.html'
    return render(request, template, context)


def recruiter_unread_notification(request, name):
    recruiter = Recruiter_Register.objects.get(username=name)

    notification = NotificationForRecruiter.objects.filter(recruiter=recruiter, is_view=False).order_by('-date')

    context = {
        'notification':notification,
        'total_notification':notification.count(),
    }
    template = 'recruiter/recruiter_unread_notification.html'
    return render(request, template, context)


def view_recruiter_notification(request, id):
    notifc = NotificationForRecruiter.objects.get(id=id)
    notifc.is_view = True
    notifc.save()

    context = {
        'notification':notifc,
    }
    template = 'recruiter/view_recruiter_notification.html'
    return render(request, template, context)


def job_application_list(request, id):
    job = Job_Post.objects.get(id=id)
    job_cv = Job_Apply.objects.filter(job=job)

    context = {
        'job':job,
        'job_cv':job_cv,
        'job_cv_count':job_cv.count(),
    }
    template = 'recruiter/job_application_list.html'
    return render(request, template, context)


def all_job_application_lists(request, name):
    recruiter = get_object_or_404(Recruiter_Register, username=name)
    cv_lists = Job_Apply.objects.filter(recruiter = recruiter)



    context = {
        'cv_lists':cv_lists,
        'count_cv_lists':cv_lists.count(),
    }
    template = 'recruiter/all_job_application_lists.html'
    return render(request, template, context)


def create_interview(request, id):
    job = get_object_or_404(Job_Post, id=id)
    recruiter = get_object_or_404(Recruiter_Register, id=request.session['recruiter_id'])

    jobs = get_object_or_404(Job_Apply, job=id)
    job_seeker = get_object_or_404(Job_Seeker_Register, username=jobs.job_seeker.username)

    if request.method == 'POST':
        message = request.POST['message']
        Create_Interview.objects.create(job=job, recruiter=recruiter, message=message)
        
        title = "Interview Notification For {}".format(job)
        message = """
        Job Title: {}
        {} <br>
        Company Name: {}

        """.format(job, message, recruiter)
        Interview_Notification.objects.create(job=job, jobseeker=job_seeker, title=title, message=message)

        return redirect('jobapp:all_job_application_lists', request.session['recruiter_name'])

    context = {
        'recruiter':recruiter,
        'job':job,
        'jobs':jobs,
        'job_seeker':job_seeker,
    }
    template = 'recruiter/create_interview.html'
    return render(request, template,context)


def reject_applicant(request, id):
    job = get_object_or_404(Job_Post, id=id)
    recruiter = get_object_or_404(Recruiter_Register, id=request.session['recruiter_id'])

    jobs = get_object_or_404(Job_Apply, job=id)
    job_seeker = get_object_or_404(Job_Seeker_Register, username=jobs.job_seeker.username)
    message = "you are rejected for this job."
    if request.method == 'POST':
        Create_Interview.objects.create(job=job, recruiter=recruiter, message=message)
        
        title = "Notification For {}".format(job)
        message = """
        Job Title: {}
        {} <br>
        Company Name: {}

        """.format(job, message, recruiter.company_name)
        Interview_Notification.objects.create(job=job, jobseeker=job_seeker, title=title, message=message)

        return redirect('jobapp:all_job_application_lists', request.session['recruiter_name'])

    context = {
        'recruiter':recruiter,
        'job':job,
        'jobs':jobs,
        'job_seeker':job_seeker,
    }
    template = 'recruiter/reject_applicant.html'
    return render(request, template,context)


def jobseeker_notification(request, name):
    jobseeker = get_object_or_404(Job_Seeker_Register, username=name)
    notifications = Interview_Notification.objects.filter(jobseeker=jobseeker).order_by('-date')

    context = {
        'notifications':notifications,
        'total_notifications':notifications.count(),
    }
    template = 'jobseeker/jobseeker_notification.html'
    return render(request, template, context)

def jobseeker_unread_notification(request, name):
    jobseeker = get_object_or_404(Job_Seeker_Register, username=name)
    notifications = Interview_Notification.objects.filter(jobseeker=jobseeker, is_view=False).order_by('-date')

    context = {
        'notifications':notifications,
        'total_unread_notifications':notifications.count(),
    }
    template = 'jobseeker/jobseeker_unread_notification.html'
    return render(request, template, context)


def jobseeker_notification_view(request, id):
    notifications = get_object_or_404(Interview_Notification, id=id)
    notifications.is_view = True
    notifications.save()

    context = {
        'notifications':notifications,
    }
    template = 'jobseeker/jobseeker_notification_view.html'
    return render(request, template, context)


def jobseeker_change_picture(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        profile_picture = request.FILES['profile_picture']
        person.picture = profile_picture
        person.save()
        messages.success(request, "Profile Picture Changed Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/jobseeker_change_picture.html'
    return render(request, template, context)


def jobseeker_about_myself(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        about_myself = request.POST['about_myself']
        person.about_me = about_myself
        person.save()
        messages.success(request, "Added About Yourself Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_about_myself.html'
    return render(request, template, context)


def jobseeker_current_address(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        current_address = request.POST['current_address']
        person.current_Adrress = current_address
        person.save()
        messages.success(request, "Added Current Address Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/address.html'
    return render(request, template, context)


def jobseeker_parmanant_address(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        parmanant_address = request.POST['parmanant_address']
        person.parmanant_Adrress = parmanant_address
        person.save()
        messages.success(request, "Added Parmanant Address Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/address.html'
    return render(request, template, context)


def jobseeker_update_about_myself(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        about_me = request.POST['my_self']
        person.about_me = about_me
        person.save()
        messages.success(request, "Update Your Information Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)
    
def jobseeker_update_current_address(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        current_address = request.POST['current_address']
        person.current_Adrress = current_address
        person.save()
        messages.success(request, "Updated Your Current Address Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)


def jobseeker_update_parmanant_address(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        parmanant_address = request.POST['parmanant_address']
        person.parmanant_Adrress = parmanant_address
        person.save()
        messages.success(request, "Updated Your Parmanant Address Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)


def jobseeker_update_fullname(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        full_name = request.POST['full_name']
        person.full_name = full_name
        person.save()
        messages.success(request, "Updated Name Successfully.")
        return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)


def jobseeker_update_email(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        email = request.POST['email']
        chk_email = Job_Seeker_Register.objects.filter(email=email).count()
        if chk_email > 0:
            messages.info(request, "This Email Already Exist.")
        else:
            person.email = email
            person.save()
            messages.success(request, "Email Changed Successfully.")
            return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)

def jobseeker_update_phone_number(request, name):
    person = get_object_or_404(Job_Seeker_Register, username=name)

    if request.method == 'POST':
        phone = request.POST['phone']
        # chk_length = phone
        chk_number = Job_Seeker_Register.objects.filter(phone_no=phone)
        # if chk_length < 12:
        #     messages.warning(request, "Your Number Must be 11 digits.")
        if chk_number:
            messages.warning(request, "This Number Already Exist.")
        else:
            person.phone_no = phone
            person.save()
            messages.success(request, "Changed Your Phone Number Successfully.")
            return redirect('jobapp:update_job_seeker_profile', name=request.session['job_seeker_name'])

    context = {
        'person':person,
    }
    template = 'jobseeker/update_profile/jobseeker_update_profile_info.html'
    return render(request, template, context)


def view_cv(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    personal_info = Create_CV_Basic_info.objects.filter(cv_jobseeker=job_seeker).first()
    career_obj = Create_CV_Career_Objective.objects.filter(cv_jobseeker=job_seeker).first()
    academic_info = Create_CV_Academic_Qualification.objects.filter(cv_jobseeker=job_seeker)
    trainings = Create_CV_Traning.objects.filter(cv_jobseeker=job_seeker)
    skills = Create_CV_Skill.objects.filter(cv_jobseeker=job_seeker).first()
    experience = Create_CV_Job_Experience.objects.filter(cv_jobseeker=job_seeker)
    hobby = Create_CV_Hobby.objects.filter(cv_jobseeker=job_seeker).first()
    language = Create_CV_Language_Profiency.objects.filter(cv_jobseeker=job_seeker)
    referance = Create_CV_Add_Referance.objects.filter(cv_jobseeker=job_seeker)
    signature = Create_CV_Signiture.objects.filter(cv_jobseeker=job_seeker).first()
    picture = Create_CV_Picture.objects.filter(cv_jobseeker=job_seeker).first()


    context = {
        'personal_info':personal_info,
        'career_obj':career_obj,
        'academic_info':academic_info,
        'trainings':trainings,
        'skills':skills,
        'experience':experience,
        'hobby':hobby,
        'language':language,
        'referance':referance,
        'signature':signature,
        'picture':picture,
    }
    template = 'jobseeker/cv/view_cv.html'
    return render(request, template, context)


def create_cv(request):
    template = 'jobseeker/cv/create_cv.html'
    return render(request, template)


def create_cv_personal_info(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        form = CV_Basic_Info_Form(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cv_jobseeker = job_seeker
            form.save()
            messages.success(request, "Basic Information Created Successfully.")
            return redirect('jobapp:create_cv_career_objective', name=request.session['job_seeker_name'])
    else:
        form = CV_Basic_Info_Form()

    context = {
        'form':form,
    }
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template, context)


def create_cv_career_objective(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        career_obj = request.POST['career_obj']
        Create_CV_Career_Objective.objects.create(cv_jobseeker=job_seeker, career_objective=career_obj)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:create_cv_academic', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)


def create_cv_academic(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        form = Create_CV_Academic_Form(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cv_jobseeker = job_seeker
            form.save()
            messages.success(request, "Successfully Created.")
            return redirect('jobapp:add_skill', name=request.session['job_seeker_name'])
    else:
        form = Create_CV_Academic_Form()
    
    context = {
        'form':form,
    }
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template, context)


def add_skill(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        skill = request.POST['skill']
        Create_CV_Skill.objects.create(cv_jobseeker=job_seeker, skill_and_specialize=skill)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:add_skill', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)


def create_training_summary(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        form = Create_CV_Traning_Form(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cv_jobseeker = job_seeker
            form.save()
            messages.success(request, "Successfully Created.")
            return redirect('jobapp:add_skill', name=request.session['job_seeker_name'])
    else:
        form = Create_CV_Traning_Form()
    
    context = {
        'form':form,
    }
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template, context)


def add_job_experience(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        form = Create_CV_Job_Experience_Form(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cv_jobseeker = job_seeker
            form.save()
            messages.success(request, "Successfully Created.")
            return redirect('jobapp:add_skill', name=request.session['job_seeker_name'])
    else:
        form = Create_CV_Job_Experience_Form()
    
    context = {
        'form':form,
    }
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template, context)


def add_hobby(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        hobby = request.POST['hobby']
        Create_CV_Hobby.objects.create(cv_jobseeker=job_seeker, hobby=hobby)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:create_cv_academic', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)


def add_language(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        language = request.POST['language']
        profiency = request.POST['profiency']
        Create_CV_Language_Profiency.objects.create(cv_jobseeker=job_seeker, language=language, profiency=profiency)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:create_cv_academic', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)


def add_referance(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        form = Create_CV_Add_Referance_Form(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.cv_jobseeker = job_seeker
            form.save()
            messages.success(request, "Successfully Created.")
            return redirect('jobapp:add_skill', name=request.session['job_seeker_name'])
    else:
        form = Create_CV_Add_Referance_Form()
    
    context = {
        'form':form,
    }
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template, context)


def add_signature(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        signature = request.FILES['signature']
        Create_CV_Signiture.objects.create(cv_jobseeker=job_seeker, signiture=signature)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:create_cv_academic', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)


def add_cv_picture(request, name):
    job_seeker = get_object_or_404(Job_Seeker_Register, username=name)
    if request.method == 'POST':
        picture = request.FILES['picture']
        Create_CV_Picture.objects.create(cv_jobseeker=job_seeker, picture=picture)
        messages.success(request, "Successfully Created.")
        return redirect('jobapp:create_cv_academic', name=request.session['job_seeker_name'])
        
    template = 'jobseeker/cv/create_cv_personal_info.html'
    return render(request, template)

