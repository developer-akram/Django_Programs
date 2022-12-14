from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dataadd',views.dataadd,name="dataadd"),
    path('update',views.update,name="update"),
    path('adddata',views.adddata,name="adddata"),
    path('viewdata',views.viewdata,name="viewdata"),
    path('deleteData',views.deleteData,name="deleteData"),
    path('applyform',views.applyform,name="applyform"),
    path('viewform',views.viewform,name="viewform"),
    path('deleteform',views.deleteform,name="deleteform"),
    path('correctionform',views.correctionform,name="correctionform"),
    path('login',views.login,name="login"),
    path('<int:course_id>/',views.feedback,name="feedback"),
    path('courselist',views.courselist,name="courselist"),
    path('showrating',views.showrating,name="showrating"),
    path('logout',views.logout,name="logout"),
]