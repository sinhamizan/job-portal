from django import template
from ..models import Category, Job_Post, Interview_Notification, Job_Seeker_Register, Create_Interview, Recruiter_Register, NotificationForRecruiter


register = template.Library()


@register.simple_tag
def get_category():
    cat = Category.objects.all()
    return cat


@register.filter
def jobseeker_nofication_count(name):
    job_seeker = Job_Seeker_Register.objects.get(username=name)
    notification = Interview_Notification.objects.filter(jobseeker=job_seeker)
    count_notification = notification.count()
    
    if count_notification > 0:
        return count_notification
    else:
        return 0

@register.filter
def total_unread_jobseeker_notifications(name):
    job_seeker = Job_Seeker_Register.objects.get(username=name)
    notification = Interview_Notification.objects.filter(jobseeker=job_seeker, is_view=False)
    count_notification = notification.count()
    
    if count_notification > 0:
        return count_notification
    else:
        return 0


@register.filter
def total_rectuiter_notifications(name):
    rectuiter = Recruiter_Register.objects.get(username=name)
    notification = NotificationForRecruiter.objects.filter(recruiter=rectuiter)
    count_notification = notification.count()
    
    if count_notification > 0:
        return count_notification
    else:
        return 0


@register.filter
def total_unread_rectuiter_notifications(name):
    rectuiter = Recruiter_Register.objects.get(username=name)
    notification = NotificationForRecruiter.objects.filter(recruiter=rectuiter, is_view=False)
    count_notification = notification.count()
    
    if count_notification > 0:
        return count_notification
    else:
        return 0


@register.filter
def interview_call(id):
    job = Create_Interview.objects.filter(job_id=id).count()
    
    if job > 0:
        return False
    else:
        return True
