from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'testimonial',
        'is_approved',
    ]
    list_filter = [
        'is_approved'
    ]
    actions = [
        'approve_testimonial'
        ]

    def approve_testimonial(self, request, queryset):
        queryset.update(is_approved=True)


admin.site.register(Testimonial, TestimonialAdmin)
