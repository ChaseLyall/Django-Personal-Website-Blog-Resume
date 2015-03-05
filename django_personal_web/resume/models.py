from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    concentration = models.CharField(max_length=200)
    gpa = models.CharField(max_length=4)
    graduation_month = models.DateField()

    def __str__(self):
        return str(self.school+' '+self.degree+' '+self.major)

class Job(models.Model):
    employer_title = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_month = models.DateField()
    end_month = models.DateField(help_text = "If current job, please set end month equal to start month.")

    def __str__(self):
        return self.employer_title

class JobDesc(models.Model):
    job = models.ForeignKey(Job)
    description = models.CharField(max_length=300)

    def __str__(self):
        return str(self.description)

class Skill_Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('Novice', 'Novice'),
        ('Proficient', 'Proficient'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Skill_Category)
    proficiency = models.CharField(max_length=200, choices=PROFICIENCY_CHOICES,)

    def __str__(self):
        return self.skill

class Leadership(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_month = models.DateField()
    end_month = models.DateField(help_text = "If role is current, please set end month equal to start month.")

    def __str__(self):
        return self.name+', '+ self.position

class LeadershipDesc(models.Model):
    leadership = models.ForeignKey(Leadership)
    description = models.CharField(max_length=300)

    def __str__(self):
        return str(self.description)

class Activity(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200)
    start_month = models.DateField()
    end_month = models.DateField(help_text = "If role is current, please set end month equal to start month.")

    def __str__(self):
        return str(self.name)

class Award(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(blank=True)

    def __str__(self):
        return str(self.name)