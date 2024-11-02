from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('post/<slug:slug>', views.single_post, name='single_post'),
    path('contact', views.contact, name='contact'),
    path('dashboard/post', views.dashboard_post, name='dashboard_post'),
    path('dashboard/post/new', views.dashboard_post_new, name='dashboard_post_new'),
    path('dashboard/post/view/<str:slug>', views.dashboard_post_view, name='dashboard_post_view'),
    path('dashboard/post/edit/<str:slug>', views.dashboard_post_edit, name='dashboard_post_edit'),
    path('dashboard/post/delete/<str:slug>', views.dashboard_post_delete, name='dashboard_post_delete'),
]


