from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, SubscriptionType, Logs
from rest_framework.authtoken.models import Token


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'phone_number', 'subscription_type', 'payed', ]
    """
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'personal_info', 'subscription_type',
                           'payed', 'configuration', )}),
    )
    """
    fieldsets = (
        (None, {'fields': ('username', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address',
                                         'personal_info', )}),
        (_('Additional info'), {'fields': ('subscription_type', 'payed', 'configuration', )}),
        # (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups', )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        print(qs)
        if not request.user.is_superuser:
            return qs.filter(is_superuser=False)
        return qs


class CustomTokenAdmin(TokenAdmin):
    model = Token

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['user'].queryset = CustomUser.objects.filter(is_superuser=False)
        return super(TokenAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SubscriptionType)
admin.site.register(Logs)

admin.site.unregister(Token)
admin.site.register(Token, CustomTokenAdmin)
