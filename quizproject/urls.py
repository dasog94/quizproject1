from django.contrib import admin
from django.urls import path
import quizapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quizapp.views.home, name="home"),
    path('submit/', quizapp.views.submit, name="submit")

]
