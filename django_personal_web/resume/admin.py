from django.contrib import admin
from resume.models import *

class JobDescInLine(admin.StackedInline):
    model = JobDesc
    extra = 1

class JobAdmin(admin.ModelAdmin):
    inlines = [JobDescInLine]
    list_display = ('employer_title', 'job_title', 'start_month', 'end_month')
    list_filter = ['end_month']
    search_fields = ['employer_title','job_title']

class SkillInLine(admin.StackedInline):
    model = Skill
    extra = 1

class SkillAdmin(admin.ModelAdmin):
    inlines = [SkillInLine]

class LeadershipDescInLine(admin.StackedInline):
    model = LeadershipDesc
    extra = 1

class LeadershipAdmin(admin.ModelAdmin):
    inlines = [LeadershipDescInLine]

#@register(Job, JobAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Education)
admin.site.register(Skill_Category, SkillAdmin)
admin.site.register(Leadership, LeadershipAdmin)
admin.site.register(Activity)
admin.site.register(Award)