
from django.urls import path
from . import views

app_name = 'branchapp'
urlpatterns = [
    path('',views.new,name='new'),
    path('var/',views.index,name='ss'),
    path('sap/',views.detail,name='detail'),
]
