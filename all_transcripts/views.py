from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from home.models import Grade, Student

def full_transcript(request):

    if request.session['member_id'] == 0:
        return redirect('/')
    else:
        return render(request, "all_transcripts/students_results.html")

def score_list(request, user_id):

    user = User.objects.get(id=user_id)
    template_path = 'all_transcripts/results_list.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if want to download 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if you want to display in the browser get rid of the attatchment
    response['Content-Disposition'] = 'filename="results_list.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def in_bulk(self, user_id):
    grades = Grade.objects.all
    user = User.objects.get(id=user_id)
    template_path = 'all_transcripts/all_transcripts.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if want to download 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if you want to display in the browser get rid of the attatchment
    response['Content-Disposition'] = 'filename="all_transcripts.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def student_transcript(request, user_id):
   
    total  = 0
    assess = 0
    exam = 0
    agg = 0
    numbers = []
    grades = []
   
    student = Student.objects.get(id=user_id)

    for d in student.grade_set.all():
       total += float(d.total_score)
       assess +=float(d.assessment_score)
       exam += round(float(d.exam_score), 2)
       numbers.append(float(d.total_score)) 
       grades.append(int(d.grade_point))
    average = total / int(len(numbers))
    grades.sort()
    my_g = grades[:5]
    for n in my_g:
       agg += n

    template_path = 'all_transcripts/student_transcript.html'
    context = {
       'student': student,
       'assess': assess,
       'exam': exam,
       'total': total,
       'average': average,
       'agg': agg,
      }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if want to download 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if you want to display in the browser get rid of the attatchment
    response['Content-Disposition'] = 'filename="all_transcripts.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
