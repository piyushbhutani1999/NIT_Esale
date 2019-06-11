from django.urls import path
from .views import product_detail_view, product_list_view, postad,product_list_view_elec,product_list_view_jobs,product_list_view_others,product_list_view_roomdecor,product_list_view_stationary,product_list_view_vehicles
from django.conf import settings
from django.conf.urls.static import static

app_name="product"

urlpatterns = [
    path("", product_list_view, name = 'home'),
    path("electonics/",product_list_view_elec, name = 'electronics'),
    path("jobs/",product_list_view_jobs, name = 'jobs'),
    path("vehicles/",product_list_view_vehicles, name = 'vehicles'),
    path("others/",product_list_view_others, name = 'others'),
    path("roomdecor/",product_list_view_roomdecor, name = 'roomdecor'),
    path("stationary/",product_list_view_stationary, name = 'stationary'),
    path("postad/",postad, name = 'postad'),
    path("<str:slug>/",product_detail_view, name = 'product_detail_view'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)