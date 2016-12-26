from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from restaurant import views
from django.views.static import serve as static_serve
from django.views.generic import TemplateView


urlpatterns = (
    # Examples:
    # url(r'^$', 'smc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")), # grappelli URLS
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    url(r'^restaurants/$',views.RestaurantListView.as_view()),
    url(r'^restaurants/(?P<pk>[\w\-]+)/?$',views.RestaurantDetailView.as_view(), name="restaurant"),
    
    url(r'media/(?P<path>.*)$',static_serve,{'document_root': settings.MEDIA_ROOT, }),
)