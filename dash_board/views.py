from django.shortcuts import render, redirect
from home.models import Student, Class, Student, Subject, Grade
from django.contrib.auth.models import User
from django.utils import dateparse
from django.contrib import messages
from datetime import datetime

def main_panel(request):

    user_id = request.session['member_id']
    today = datetime.now()

    if user_id == 0:
        return redirect('/')
    else:
        the_user = User.objects.get(id=user_id)
        context = {
            'the_user':the_user,
            'today':today,
        }

    if user_id  == 0:
        return redirect("/")
    else:
        return render(request, "dash_board/main.html", context)

def subject_upload(request):

    try:
        subject_code = request.POST['subject_code']
        subject_name = request.POST['subject_name']
        user_id = request.POST['user_id']

    except KeyError:
        messages.info(request, "invalid user_id")
        return redirect("dash_board:main_panel")
    else:
        if Subject.objects.filter(subject_code=subject_code).exists():
            messages.info(request, "ERROR! Subject Code " + subject_code + " already exists")
            return redirect("dash_board:main_panel")

        else:
            user = User.objects.get(id=user_id)
            subject = Subject.objects.create(
                teacher=user,
                subject_code=subject_code,
                subject_name=subject_name,
            )
            subject.save()
            messages.info(request, "Subject added successfully!")
            return redirect("dash_board:main_panel")

def add_student(request):

    class_id = request.POST['class_id']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    gender = request.POST['gender']
    date = request.POST['date']
    parent_phone = request.POST['parent_phone']
    parent_email = request.POST['parent_email']
    profile_photo = request.FILES['profile_photo']


    my_class = Class.objects.get(id=class_id)

    student = Student.objects.create(
        stage=my_class,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        gender=gender,
        dob=date,
        parent_phone=parent_phone,
        prarent_email=parent_email,
        passport_pic=profile_photo
    )
    student.save()
    messages.info(request, "Student, " + first_name + " added successfully")
    return redirect("dash_board:main_panel")

def all_students(request, class_id):

    stage = Class.objects.get(id=class_id)

    context = {
        'stage':stage
    }

    if stage.teacher.id != request.session['member_id']:
        return redirect('/dash_board/' + str(request.session['member_id']) + '/all_students')
    else:
        return render(request, "home/student_profiles.html", context)

def subjects(request):

    if request.session['member_id'] == 0:
        return redirect('/')
    else:
        return render(request, "home/subjects.html")

def subject_delete(request):

    try:
        my_subject = Subject.objects.get(pk=request.POST['subject'])
        my_subject.delete()
    except KeyError:
        messages.info(request, "You did not select any subject")
        return redirect('dash_board:subjects')
    else:
        messages.info(request, "Subject deleted successfully")
        return redirect("dash_board:subjects")

def edit_subject(request):

    subject_id = request.POST['subject_id']
    subject_code = request.POST['subject_code']
    subject_name = request.POST['subject_name']

    try:
        subject = Subject.objects.get(id=subject_id)
    except KeyError:
        messages.info(request, "Invalid action")
        return redirect("dash_board:subjects")
    else:
        subject.subject_name = subject_name
        subject.subject_code = subject_code
        subject.save()
        messages.info(request, "Subject edited successfully") 
        return redirect("dash_board:subjects")

def edit_profile(request):

    stage_id = request.POST['stage_id']
    student_id = request.POST['student_id']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    gender = request.POST['gender']
    parent_phone = request.POST['parent_phone']
    parent_email = request.POST['parent_email']
    

    student = Student.objects.get(pk=student_id)
    student.first_name = first_name
    student.middle_name = middle_name
    student.last_name = last_name
    student.gender = gender
    student.parent_phone = parent_phone
    student.parent_email = parent_email
    student.save()

    messages.info(request, "Profile edited successfully!")
    return redirect('/dash_board/' + str(stage_id) + '/all_students')

def add_score(request):

    student_id = request.POST['student_id']
    subject = request.POST['subject']


    try:
        my_subject = Subject.objects.get(id=subject)
    except ValueError:
        messages.info(request, "You did not select any subject...try again !")
        return redirect("dash_board:main_panel")

    student = Student.objects.get(id=student_id)

    assess = request.POST['assessment']
    ex = request.POST['exam']

    if assess == "":
        assess = 0
    if ex == "":
        ex = 0

    assessment = float(assess)
    exam = float(ex) * 60  / 100
    
    if Grade.objects.filter(student=student, Subject=my_subject).exists():
        messages.info(request, "Grade for this subject already Uploaded")
        return redirect("dash_board:main_panel")

    if assessment < 0 or assessment > 40:
        messages.info(request, "Assessment can not be greater than 40 or less than 0")
        return redirect("dash_board:main_panel")

    if float(request.POST['exam']) < 0 or float(request.POST['exam']) > 100:
        messages.info(request, "Exam score cannot be greater than 100 or less than 0")
        return redirect("dash_board:main_panel")
    else:
        grade = Grade.objects.create(
            student=student,
            Subject=my_subject,
            assessment_score=assessment,
            exam_score=exam,
        )
        grade.save()
        messages.info(request, "Grade uploaded successfully!")
        return redirect("dash_board:main_panel")

def edit_score_page(request, student_id):

    student = Student.objects.get(id=student_id)
    std_id = student.stage.teacher.id

    context = {
        'student':student,
    }

    if request.session['member_id'] == std_id:
        return render(request, 'dash_board/edit_score_page.html', context)
    else:
        return redirect('/dash_board/' + str(request.session['member_id']) + '/edit_score_page')

def edit_score(request):

    student_id = request.POST['student_id']
    grade_id = request.POST['grade_id']
    assess = request.POST['assess']
    exam = float(request.POST['exam'])

    grade = Grade.objects.get(id=grade_id)
    grade.assessment_score = assess
    grade.exam_score = exam
    grade.save()

    messages.info(request, "Grade edited successfully")
    return redirect('/dash_board/' + str(student_id) + '/edit_score_page')