from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path("", views.index, name='index'),
    # /polls/5
    path('<int:question_id>', views.detail, name='index'),
    # /polls/results/5
    path('results/<int:question_id>/', views.results, name='index'),
    # /polls/vote/5
    path('vote/<int:question_id>/', views.vote, name='index'),
]
