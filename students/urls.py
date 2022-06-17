from django.urls import path,include

from . import views

from rest_framework import routers
router=routers.DefaultRouter()
router.register('university',viewset=views.UniversityViewset)
router.register('students',viewset=views.StudentViewset)

urlpatterns = [
    path('', include(router.urls))
#     path('createuniversity', views.createuniversity),
#     path('alluniversity', views.alluniversity),
#     path('create', views.create),
#     path('all', views.all),
#     path('update',views.update),
#     path('delete',views.delete),
]