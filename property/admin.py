from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerNameshipInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by', )
    inlines = [
        OwnerNameshipInline,
    ]


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', )
    inlines = [
        OwnerNameshipInline,
    ]
    exclude = ["flat"]


admin.site.register(Owner, OwnerAdmin)
