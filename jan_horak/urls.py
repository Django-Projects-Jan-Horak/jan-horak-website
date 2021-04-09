"""jan_horak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from projects import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    # Basic
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    # Web
    path('web', views.web_development, name="web_development"),
    path('web/<str:name>', views.webprojects, name="webprojects"),
    path('web/project/<int:id>/', views.detail_web, name='detail_web'),

    # Games
    path('games', views.game_development, name="game_development"),
    path('games/<str:name>', views.gameprojects, name="gameprojects"),
    path('games/project/<int:id>/', views.detail_game, name='detail_game'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
