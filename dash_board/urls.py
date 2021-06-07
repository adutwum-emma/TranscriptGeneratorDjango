from django.urls import path
from . import views

app_name = "dash_board"

urlpatterns = [
    path('main_panel', views.main_panel, name="main_panel"),
    path('subject_upload', views.subject_upload, name="subject_upload"),
    path('add_student', views.add_student, name="add_student"),
    path('<int:class_id>/all_students', views.all_students, name="all_students"),
    path('subjects', views.subjects, name="subjects"),
    path('subject_delete', views.subject_delete, name="subject_delete"),
    path('edit_subject', views.edit_subject, name="edit_subject"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('add_score', views.add_score, name="add_score"),
    path('edit_score', views.edit_score, name="edit_score"),
    path('<int:student_id>/edit_score_page', views.edit_score_page, name="edit_score_page"),
]