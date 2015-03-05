from django.shortcuts import render
from django.http import HttpResponse

from resume.models import *

def resume(request):
    job_list = Job.objects.order_by('-end_month')
    education_list = Education.objects.order_by('-graduation_month')
    skill_list = Skill_Category.objects.all()
    leadership_list = Leadership.objects.order_by('-end_month')
    activity_list = Activity.objects.order_by('-end_month')
    award_list = Award.objects.order_by('-date')
    context = {'job_list': job_list,
               'education_list': education_list,
               'skill_list': skill_list,
               'leadership_list': leadership_list,
               'activity_list': activity_list,
               'award_list': award_list}
    return render(request, 'resume/resume.html', context)