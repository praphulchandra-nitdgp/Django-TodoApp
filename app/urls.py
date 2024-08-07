from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]





# from django.http import HttpResponse
# from django.urls import path

# def test_logout(request):
#     return HttpResponse("Logout URL is reachable.")

# urlpatterns = [
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', test_logout, name='logout'),  # Add this line
#     path('', TaskList.as_view(), name='tasks'),
#     path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
#     path('task-create/', TaskCreate.as_view(), name='task-create'),
#     path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
#     path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
# ]
