from django.urls import path
from . import views


app_name = 'polls'


urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name='index'),
    # /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # /polls/results/5
    path('results/<int:pk>/', views.ResultView.as_view(), name='results'),
    # /polls/vote/5
    path('vote/<int:question_id>/', views.vote, name='vote'),
]
