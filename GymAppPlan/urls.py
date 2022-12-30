"""GymAppPlan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Accounts import views
from App.views import MainPageView, AddExerciseView, ExerciseList, ExerciseView, AddPlanView, PlanList, PlanView, \
    AddToPlanView, AddPrView, PrsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('main_page', MainPageView.as_view(), name='main_page'),
    path('add_exercise/', AddExerciseView.as_view(), name='add_exercise'),
    path('list_exercise/', ExerciseList.as_view(), name='list_exercise'),
    path('exercise/<int:id>/', ExerciseView.as_view(), name='exercise_view'),
    path('exercise/<int:id>/add_pr', AddPrView.as_view(), name='add_pr'),
    path('exercise/<int:id>/view_pr', PrsView.as_view(), name='pr_list'),
    path('exercise/<int:id>/add_to_plan/', AddToPlanView.as_view(), name='add_to_plan'),
    path('add_plan/', AddPlanView.as_view(), name='add_plan'),
    path('list_plan/', PlanList.as_view(), name='list_plan'),
    path('plan/<int:id>/', PlanView.as_view(), name='plan_view'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add_user/', views.AddUserView.as_view(), name='add_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
