from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('login_index/', views.login_index, name='movies.login_index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
    path('movie/<int:movie_id>/hide/', views.hide_movie, name='movies.hide_movie'),
    path('hidden/', views.hidden_movies_list, name='movies.hidden_movies_list'),
    path('movie/<int:movie_id>/unhide/', views.unhide_movie, name='movies.unhide_movie'),
]