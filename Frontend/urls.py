from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.login_page, name="login"),

    path('index/', views.index_page, name="index"),
    path('signup/', views.signup_page, name="signup"),

    path('saveuserdata/', views.user_signup, name="save_user_data"),
    path('loginvalidate/', views.login_validate, name="login_validate"),
    path('userlogout/', views.user_logout, name="logout"),
    path('update_task/<int:task_id>/', views.update_task, name="update_task"),
    # path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    # path('delete_all_task/', views.delete_all_task, name="delete_all_task"),
]