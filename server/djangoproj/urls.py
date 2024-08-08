"""djangoproj URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
    path('login/', TemplateView.as_view(template_name="index.html"), name='login_page'),
    # path('logout/', TemplateView.as_view(template_name="Home.html"), name='logout_page'),
    path('register/', TemplateView.as_view(template_name="index.html"), name='register_page'),

    path('djangoapp/', include('djangoapp.urls')),  # Assumes djangoapp.urls is properly set up
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),  # Home page route
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

