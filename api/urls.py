from django.urls import path
from . import views
urlpatterns = [
    path("items",views.items,name="items"),
    path("booking",views.booking,name="booking"),
    path("cancel",views.cancelslot,name="cancel"),
    path("plot",views.plot,name="plot")
]