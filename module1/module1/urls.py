from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('meme.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]

admin.site.site_header = "Stonks Admin"
admin.site.site_title = "Stonks Admin Portal"
admin.site.index_title = "Welcome to Stonks Portal"         
