"""
URL configuration for luminar project.

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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from luminarapi import views as api_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


from adminapp import views as admin_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi






# Define the schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)



from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
# router.register("api/register",api_view.UsersView,basename="users"),
# router.register("api/courses",api_view.CoursesListView,basename="courses"),
router.register("api/student/demovideo",api_view.DemoClassListView,basename="demovideo"),
router.register("api/student/courses",api_view.DetailsListAPIView,basename="courses"),
# router.register("api/modules",api_view.ModulesAPIView,basename="modules"),

router.register("api/student/batches",api_view.BatchListView,basename="batches"),

router.register("api/student/overview",api_view.OverDetailView,basename="overview"),
router.register("api/student/attendance",api_view.AttendanceView,basename="attendance"),
router.register("api/student/assignment",api_view.AssignmentView,basename="assignment"),
router.register("api/student/announcement",api_view.AnnouncementView,basename="announcement"),
router.register("api/student/liveclass",api_view.LiveClassView,basename="liveclass"),
router.register("api/student/videoclass",api_view.VideoScreenView,basename="videoclass"),
router.register("api/student/test",api_view.TestView,basename="test"),
router.register("api/student/jobportal",api_view.JobPortalView,basename="jobportal"),

router.register('api/register',admin_view.CustomAdminView,basename="admins")
router.register('api/student/register',admin_view.StudentView,basename="students")
router.register('api/waitinglists',admin_view.WaitingListView,basename="waitinglists")
router.register('api/batches',admin_view.BatchView,basename="batches")
router.register('api/addedstudents',admin_view.AddedView,basename="addedstudents")

# router.register("api/admin/adddemovideo",api_view.VideoScreenClassViewSet,basename="adddemovideo"),
router.register("api/admin/logo",api_view.LogoViewSet,basename="logo"),
router.register("api/admin/module",api_view.ModuleView,basename="module"),


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/login/",ObtainAuthToken.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('batch/<int:batch_id>/add-student/', admin_view.AddStudentToBatch.as_view(), name='add-student-to-batch'),
   
   
    # path('api/password-reset/<int:id>/',api_view.PasswordReset),
    # path("api/verifyotp/<int:id>/", api_view.VerifyOtp),
  
    # path("api/resetpassword/<int:id>/", api_view.Resetpassword),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("", include(router.urls))

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
