from django.urls import path
from . import views

app_name = "all_transcripts"

urlpatterns = [
    path('full_transcript', views.full_transcript, name="full_transcript"),
    path('<int:user_id>score_list', views.score_list, name="score_list"),
    path('<int:user_id>/in_bulk', views.in_bulk, name="in_bulk"),
    path('<int:user_id>/student_transcript', views.student_transcript, name="student_transcript"),
]