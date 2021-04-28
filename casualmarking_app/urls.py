from django.urls import path
from .views import index, admin, create_marker, create_student

urlpatterns = [
    path('', index, name="index"),
    path('admin_page/', admin, name="admin_page"),
    path('create_marker/', create_marker, name="create_marker"),
    path('create_student/', create_student, name="create_student"),
]