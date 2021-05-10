"""the_rapper URL Configuration

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
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from artist.views_api import ArtistViewSet
from single.views_api import SingleViewSet

router = DefaultRouter()
router.register(r'artist', ArtistViewSet, basename='artist')
router.register(r'single', SingleViewSet, basename='single')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('artists', ArtistViewSet.artist_list, name='artist-list'),
    path('artists/<int:artistId>', ArtistViewSet.artist_detail, name='artist-detail'),

    # path('artists/', ArtistViewSet.all, name='artist-all'),
    # path('artist', ArtistViewSet.create, name='artist-create'),
    # # path('artist/id/<int:artistId>', ArtistViewSet.getByID, name='artist-by-id'),
    # path('artist/<int:artistId>', ArtistViewSet.remove, name='artist-remove'),
    # path('artists/<int:artistId>', ArtistViewSet.update, name='artist-update'),

    #get_artist_by_id

    path('singles/', SingleViewSet.all, name='single-all'),
    path('single', SingleViewSet.create, name='single-create')
    #delete_single_by_id
]
