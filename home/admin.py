from django.contrib import admin
from .models import Contact, Faq


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )


admin.site.register(Contact, ContactAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'is_active',
    )


admin.site.register(Faq, FaqAdmin)
