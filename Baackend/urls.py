from django.urls import path
from Baackend import views

urlpatterns = [
    path('admin_page/', views.admin_page, name="admin_page"),
    path('employee_list/', views.employee_details, name="employee_list"),
    path('task/', views.assign_task_page, name="assign_task_page"),
    path('assign_task/', views.assign_task, name="assign_task"),
    path('view_task/<emp_name>/', views.view_task, name="view_task"),
    path('view_all_task/', views.view_all_task, name="view_all_task"),
    path('remove_task/<int:emp_id>/', views.remove_task, name="remove_task"),
    # path('admin_login/', views.admin_login_page, name="admin_login_page"),
    # path('admin_login_validate/', views.admin_login_validate, name="admin_login_validate"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
]