"""superlists URL Configuration

The `urlpatterns` list4 routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
## using 2.0- regex 4to match url
## import url or re_path
from django.conf.urls import url
from django.conf import settings
from lists import views

urlpatterns = [
    ## (.+) means a captured group, it will capture any characters that's following /.
    ## captured text is going to be delievered as arguments
    ## the argument will pass inhidden with test_can_save_a_POST_request
    ## e.g. /lists/foo/ --> view as view_list(request, "foo")
    ## also (.+) is one greedy regex almost matching everything
    url(r'^(\d+)/$',views.view_list, name='view_list'),
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/add_item$',views.add_item, name='add_item'),
]
