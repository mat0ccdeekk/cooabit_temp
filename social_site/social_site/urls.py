"""social_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('chat/', include('django_private_chat.urls')),
    path('app/', include('custom_app.urls')),
    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('home.urls')),
    path('pay/', include('pay.urls')),

    url(r'^chat/', include('chat.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^messages/', views.messages, name='messages'),
    url(r'^message/(?P<selected_user>\w+)/$', views.message, name='messages'),
    url(r'^api/messages/', views.messagesApi, name='messagesApi'),
    url(r'^api/message/(?P<selected_user>\w+)/$', views.messageApi, name='messagesApi'),
#
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
