from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('result/', views.result, name='result'),
    path('collect/', views.collect, name='collect'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('go_back/', views.go_back, name='go_back'),
    path('beginner/', views.beginner, name='beginner'),
    path('advanced/', views.advanced, name='advanced'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_signin/', views.user_signin, name='user_signin'),
    path('intermediate/', views.intermediate, name='intermediate'),
    path('posedetection/', views.posedetection, name='posedetection'),
    path('levelselection/', views.levelselection, name='levelselection'),
    path('tree-knowledge/', views.tree_knowledge, name='tree-knowledge'),
    path('plank-knowledge/', views.plank_knowledge, name='plank-knowledge'),
    path('cobra-knowledge/', views.cobra_knowledge, name='cobra-knowledge'),
    path('goddess-knowledge/', views.goddess_knowledge, name='goddess-knowledge'),
    path('downdog-knowledge/', views.downdog_knowledge, name='downdog-knowledge'),
    path('triangle-knowledge/', views.triangle_knowledge, name='triangle-knowledge'),
    path('warrior1-knowledge/', views.warrior1_knowledge, name='warrior1-knowledge'),
    path('warrior2-knowledge/', views.warrior2_knowledge, name='warrior2-knowledge'),
    path('warrior3-knowledge/', views.warrior3_knowledge, name='warrior3-knowledge'),
]