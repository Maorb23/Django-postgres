from django.urls import path

from . import views

"""
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
#version 2 with generic views


#urlpatterns = [
 #   path('', views.index, name='index'),
  #  path('<int:question_id>/', views.detail, name='detail'),
   # path('<int:question_id>/results/', views.results, name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#]

<<<<<<< HEAD
from django.urls import path

from . import views

app_name = 'Maor_proj.polls'
=======
app_name = 'polls'
>>>>>>> 58a037ee7c22b28c992f9c32e1a03fb55343b9d2
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
