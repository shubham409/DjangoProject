"""drfconcepts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path , include

from drf_auth_perm.views import (
    # AllStudentsModelViewSet,
    # StaffStudentsModelViewSet,
    # ReadonlyStudentsModelViewSet,
    TokenStudentModelViewSet,
    GetCustomToken,
    

    )
from rest_framework.routers import DefaultRouter

# for getting in build view to get token 
from rest_framework.authtoken.views import obtain_auth_token





# router1 = DefaultRouter()
# router1.register('',AllStudentsModelViewSet,basename='students')

# router2 = DefaultRouter()
# router2.register('',ReadonlyStudentsModelViewSet,basename='students')

# router3 = DefaultRouter()
# router3.register('',StaffStudentsModelViewSet,basename='students')



router = DefaultRouter()
router.register('',TokenStudentModelViewSet,basename='students')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',include('customapi.urls')),
    path('api/',include('queryapi.urls')),
    # path('all/',include(router1.urls)),
    # path('read/',include(router2.urls)),
    # path('staff/',include(router3.urls))
    path('gettoken/',obtain_auth_token),
    path('custom/',GetCustomToken.as_view()),
    path('tokenauth/',include(router.urls))

]






