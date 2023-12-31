"""
URL configuration for DropoutsAnalyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from Report.views import SchoolView, StudentView, DropoutView,FilterStudents_state,FilterStudents_city,FilterStudents_caste,FilterStudents_school

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('schools/', SchoolView.as_view(), name='schools'),
    path('students/', StudentView.as_view(), name='students'), 
    path('dropouts/', DropoutView.as_view(), name='dropouts'),
    path('filter/state', FilterStudents_state.as_view(), name='filter_state'),
    path('filter/city', FilterStudents_city.as_view(), name='filter_city'),
    path('filter/school', FilterStudents_school.as_view(), name='filter_school'),
    path('filter/caste', FilterStudents_caste.as_view(), name='filter_caste'),
]

