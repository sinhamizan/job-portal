from django.urls import path
from . import views

app_name='jobapp'
urlpatterns = [
    path('', views.Home, name='home'),
    path('do-registration', views.do_registration, name='do_registration'),
    path('do-login', views.do_login, name='do_login'),

    path('recruiter-register', views.recruiter_register, name='recruiter_register'),
    path('job-seeker-register', views.job_seeker_register, name='job_seeker_register'),

    path('recruiter-login', views.recruiter_login, name='recruiter_login'),
    path('job-seeker-login', views.job_seeker_login, name='job_seeker_login'),

    path('recruiter-logout', views.recruiter_logout, name='recruiter_logout'),
    path('job-seeker-logout', views.job_seeker_logout, name='job_seeker_logout'),

    path('jobs', views.all_job, name='all_job'),
    path('job/<int:id>', views.job_detail, name='job_detail'),

    path('recruiter/<name>', views.recruiter_profile, name='recruiter_profile'),
    path('job-seeker/<name>', views.job_seeker_profile, name='job_seeker_profile'),

    path('recruiter-update-profile/<name>', views.update_recruiter_profile, name='update_recruiter_profile'),
    path('job-seeker-update-profile/<name>', views.update_job_seeker_profile, name='update_job_seeker_profile'),

    path('post-job', views.post_job, name='post_job'),
    path('edit-job/<int:id>', views.edit_job, name='edit_job'),
    path('delete-job/<int:id>', views.delete_job, name='delete_job'),
    path('apply-job/<int:id>', views.apply_job, name='apply_job'),

    path('recruiter-posted-job/<name>', views.recruiter_posted_job, name='recruiter_posted_job'),

    path('todays-jobs', views.todays_job, name='todays_job'),
    path('category/<name>', views.category_wise, name='category_wise'),
    path('company/<name>', views.company_wise, name='company_wise'),

    path('searched-jobs', views.job_search_page, name='job_search_page'),

    path('blog-posts', views.blog_posts, name='blog_posts'),
    path('single-post/<int:id>', views.single_post, name='single_post'),

    path('error-message', views.error_message, name='error_message'),
    path('welcome-message', views.welcome_message, name='welcome_message'),

    path('application-list/<name>', views.application_list, name='application_list'),

    path('change-password/<name>/', views.jobseeker_change_password, name='jobseeker_change_password'),
    path('recruiter-change-password/<name>/', views.recruiter_change_password, name='recruiter_change_password'),

    path('recruiter-notification/<name>/', views.recruiter_notification, name='recruiter_notification'),
    path('recruiter-unread-notification/<name>/', views.recruiter_unread_notification, name='recruiter_unread_notification'),
    path('view-recruiter-notification/<int:id>/', views.view_recruiter_notification, name='view_recruiter_notification'),

    path('job/<int:id>/application-list', views.job_application_list, name='job_application_list'),

    path('application-lists/<name>', views.all_job_application_lists, name='all_job_application_lists'),

    path('create-interview/<int:id>', views.create_interview, name='create_interview'),

    path('reject-applcant/<int:id>', views.reject_applicant, name='reject_applicant'),

    path('jobseeker-notification/<name>', views.jobseeker_notification, name='jobseeker_notification'),
    path('jobseeker-unread-notification/<name>', views.jobseeker_unread_notification, name='jobseeker_unread_notification'),
    path('jobseeker-notification/<int:id>/view', views.jobseeker_notification_view, name='jobseeker_notification_view'),

    path('jobseeker/<name>/change-picture', views.jobseeker_change_picture, name='jobseeker_change_picture'),
    path('jobseeker/<name>/about-myself', views.jobseeker_about_myself, name='jobseeker_about_myself'),

    path('jobseeker/<name>/current-address', views.jobseeker_current_address, name='jobseeker_current_address'),
    path('jobseeker/<name>/parmanent-address', views.jobseeker_parmanant_address, name='jobseeker_parmanant_address'),

    path('jobseeker/<name>/update-about-myself', views.jobseeker_update_about_myself, name='jobseeker_update_about_myself'),

    path('jobseeker/<name>/update-current-address', views.jobseeker_update_current_address, name='jobseeker_update_current_address'),

    path('jobseeker/<name>/update-parmanent-address', views.jobseeker_update_parmanant_address, name='jobseeker_update_parmanant_address'),
    
    path('jobseeker/<name>/update-full-name', views.jobseeker_update_fullname, name='jobseeker_update_fullname'),
    
    path('jobseeker/<name>/update-email', views.jobseeker_update_email, name='jobseeker_update_email'),

    path('jobseeker/<name>/update-phone-number', views.jobseeker_update_phone_number, name='jobseeker_update_phone_number'),

    path('view-cv/<name>', views.view_cv, name='view_cv'),
    path('create-cv', views.create_cv, name='create_cv'),

    path('create-cv-personal-info/<name>', views.create_cv_personal_info, name='create_cv_personal_info'),
    path('create-cv-career-objective/<name>', views.create_cv_career_objective, name='create_cv_career_objective'),
    path('create-cv-academic-qualification/<name>', views.create_cv_academic, name='create_cv_academic'),
    path('add-skill/<name>', views.add_skill, name='add_skill'),
    path('create-training-summary/<name>', views.create_training_summary, name='create_training_summary'),
    path('add-job-experience/<name>', views.add_job_experience, name='add_job_experience'),
    path('add-hobby/<name>', views.add_hobby, name='add_hobby'),
    path('add-language/<name>', views.add_language, name='add_language'),
    path('add-referance/<name>', views.add_referance, name='add_referance'),
    path('add-referance/<name>', views.add_referance, name='add_referance'),
    path('add-cv-picture/<name>', views.add_cv_picture, name='add_cv_picture'),
    path('add-signature/<name>', views.add_signature, name='add_signature'),
    



]