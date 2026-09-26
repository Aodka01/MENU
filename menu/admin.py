from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from .models import Dish


@admin.action(description='Ocultar platillos del menú público')
def hide_dishes(modeladmin, request, queryset):
    updated = queryset.update(available=False)
    modeladmin.message_user(
        request,
        f'{updated} platillo(s) oculto(s) del menú público.',
        messages.SUCCESS,
    )


@admin.action(description='Mostrar platillos en el menú público')
def show_dishes(modeladmin, request, queryset):
    updated = queryset.update(available=True)
    modeladmin.message_user(
        request,
        f'{updated} platillo(s) mostrado(s) en el menú público.',
        messages.SUCCESS,
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'visibility_status')
    list_filter = ('available',)
    search_fields = ('name', 'description')
    actions = (hide_dishes, show_dishes)
    actions_on_top = True
    actions_on_bottom = True

    @admin.display(description='Visibilidad', ordering='available')
    def visibility_status(self, obj):
        if obj.available:
            return format_html('<strong style="color: #16803c;">Visible</strong>')
        return format_html('<strong style="color: #c62828;">Oculto</strong>')
