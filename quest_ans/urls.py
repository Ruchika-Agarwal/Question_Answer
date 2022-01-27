"""quest_ans URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mcq import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('select_category/',views.select_category,name="select_category"),
    path('textall_categories/',views.textall_categories,name="textall_categories"),
    path('imgall_categories/',views.imgall_categories,name="imgall_categories"),
    path('textcategory_questions/<int:cat_id>',views.textcategory_questions,name="textcategory_questions"),
    path('submit_ans/<int:cat_id>/<int:quest_id>/',views.submit_ans,name="submitAns"),

    path('imgcategory_questions/<int:cat_id>/',views.imgcategory_questions,name="imgcategory_questions"),
    path('submit_ans1/<int:cat_id>/<int:quest_id>/',views.submit_ans1,name="submitAns1"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
