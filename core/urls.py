from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('techno/', views.get_technologies, name='get-technologies'),
    path('testimonials/', views.get_testimonials, name='get-testimonials'),
    path('portfolio', views.get_portfolio, name='get-portfolio'),

    path('testimonial/', views.create_testimonial, name='testimonial-add'),
    path('testimonial/<str:pk>', views.update_testimonial, name='testimonial-edit'),
    path('del-testimonial/<str:pk>',
         views.delete_testimonial, name='del-testimonial'),

    path('add-category/', views.create_category, name='add-category'),
    path('edit-category/<str:pk>', views.update_category, name='edit-category'),
    path('del-category/<str:pk>', views.delete_category, name='del-category'),

    path('project/<str:slug>/', views.get_project, name='project'),
    path('add-project/', views.create_project, name='add-project'),
    path('edit-project/<str:pk>', views.update_project, name='edit-project'),
    path('del-project/<str:pk>', views.delete_project, name='del-project'),
]

htmx_urlpatterns = [
    path('load_preview_logo/', views.load_preview_logo, name='preview-logo'),
    path('clear-alert/', views.clear_alert, name='clear-alert'),

    path('technology-form/', views.technology_form,
         name='technology-form'),
    path('add-technology/', views.create_technology, name='add-tech'),

    path('thirdparty-form/', views.thirdparty_form, name='thirdparty-form'),
    path('add-thirdparty/', views.create_thirdparty, name='add-thirdparty'),

    path('get-projects/', views.get_projects, name='get-projects'),

    path("consult/", views.consult, name='consult'),

    path('get-certificates/', views.get_certificates, name='get-certificates'),
    path('create-certificate/', views.create_certificate,
         name='create-certificate'),
]

urlpatterns += htmx_urlpatterns
