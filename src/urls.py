from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from src.views import tour_views

urlpatterns = [
    path('', tour_views.main_page , name="main-page"),
    path('tour/<int:id>/',tour_views.tour , name="tour" ),
    path('gallery/', tour_views.gallery, name="gallery"),
    path('about/', tour_views.about, name="about")
]


