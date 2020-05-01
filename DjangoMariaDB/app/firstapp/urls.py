from django.urls import path

from . import views

urlpatterns = [
    #path('', views.paito, name='paito'),
    # ex: /1.0/5/
    #path('states/<int:id>/', views.state, name='state'),
    #path('states/', views.states, name='states'),
    #path('movie/get/', views.movies, name='movies'),
    #path('moviespost/post/', views.movies, name='movies'),
    path('generate_password/<str:password>/',views.makepassword,name='makepassword'),
    path('client/list/', views.showMovies, name = 'showMovies'),
    path('', views.vista, name = 'vista'),
    path('',views.vista,name='vista'),
    path('dos.html',views.vista2,name='vista2'),
    #path('client/update/', views.updateclient, name='updateclient'),
    #path('client/get/', views.getclient, name='getclient'),
    #path('client/delete/', views.deleteclient, name='deleteclient'),

]
