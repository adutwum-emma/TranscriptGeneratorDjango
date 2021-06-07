from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):

    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    name_of_class = models.CharField(max_length=200)
    class_code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name_of_class + " " + self.class_code + "_" + self.teacher.first_name

    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['name_of_class']

class Student(models.Model):

    stage = models.ForeignKey(Class, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    parent_phone = models.CharField(max_length=100)
    prarent_email = models.CharField(max_length=200, null=True, blank=True)
    passport_pic = models.ImageField(upload_to="profile_photos")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "Students"

class Subject(models.Model):
    student = models.ManyToManyField(Student, through='Grade')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=100, unique=True)
    subject_name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.subject_name +  "_" + self.subject_code

    class Meta:
        verbose_name_plural = "Subjects"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment_score = models.FloatField(null=True, blank=True)
    exam_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.student.first_name + " " + str(self.total_score)
        

   
    @property
    def the_grade(self):
        
        if self.total_score >= 80:
            return "A"
        if self.total_score >=70 and self.total_score < 80:
            return "B"
        if self.total_score >=60 and self.total_score < 70:
            return "C"
        if self.total_score >=50 and self.total_score < 60:
            return "D"
        if self.total_score >=40 and self.total_score <=50:
            return "E"
        else:
            return "F"

    @property
    def remarks(self):
        if self.total_score >= 80:
            return "Excellent"
        if self.total_score >=70 and self.total_score <89:
            return "V. Good"
        if self.total_score >=60 and self.total_score <= 70:
            return "Good"
        if self.total_score >=50 and self.total_score <=60:
            return "Credit"
        if self.total_score >=40 and self.total_score <=50:
            return "Pass"
        else:
            return "Fail"
    
    @property 
    def total_score(self):
        return float(self.assessment_score) + float(self.exam_score)

    @property
    def total_mark(self):
        total = 0
        numbers = []
        numbers.append(self.total_score)
        for i in numbers:
            total += float(i)
        return total

    @property
    def grade_point(self):
        if self.total_score >= 80:
            return 1
        if self.total_score >=70 and self.total_score <89:
            return 2
        if self.total_score >=60 and self.total_score <= 70:
            return 3
        if self.total_score >=50 and self.total_score <=60:
            return 4
        if self.total_score >=40 and self.total_score <=50:
            return 5
        else:
            return 6
    
    class Meta:
        verbose_name_plural = "Grades"
        ordering = ['Subject']


class SchoolLogo(models.Model):
    file_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="school_logos")

    def __str__(self):
        return self.file_name