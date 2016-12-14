from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from restaurant import views
from django.views.static import serve as static_serve


urlpatterns = (
    # Examples:
    # url(r'^$', 'smc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT,}),

    url(r'^$',views.base),
    url(r'^restaurants/$',views.index),
    url(r'^restaurants/(?P<slug>[\w\-]+)/?$',views.fetch_restaurant),

)