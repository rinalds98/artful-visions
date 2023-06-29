from django.urls import path
from .views import discount_validation

urlpatterns = [
    path(
        "validate-discount/",
        discount_validation,
        name="discount_validation",
    ),
]
