from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cases/', views.cases, name='cases'),
    path('plaintiffs/', views.plaintiffs, name='plaintiffs'),
    path('defendants/', views.defendants, name='defendants'),
    path('new_case/', views.new_case, name='new_case'),
    path('new_plaintiff/', views.new_plaintiff, name='new_plaintiff'),
    path('new_defendant/', views.new_defendant, name='new_defendant'),
    path('case/<uuid:case_id>/', views.case, name='case'),
    path('plaintiff_detail/<uuid:plaintiff_id>', views.plaintiff_detail, name='plaintiff_detail'),
    path('defendant_detail/<uuid:defendant_id>', views.defendant_detail, name='defendant_detail'),
    path('edit_case/<uuid:case_id>/', views.edit_case, name='edit_case'),
    path('edit_plaintiff/<uuid:plaintiff_id>/', views.edit_plaintiff, name='edit_plaintiff'),
    path('edit_defendant/<uuid:defendant_id>/', views.edit_defendant, name='edit_defendant'),
    path('make_petition/<uuid:case_id>/', views.make_petition_view, name='make_petition_view'),
]
