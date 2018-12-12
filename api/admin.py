from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'phone', 'email', 'address', )
    list_display = ('first_name', 'last_name', 'phone', 'email', 'address', )
    list_filter = ['first_name']

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProfileAdmin, self).get_form(request, obj, **kwargs)
        # Show only unassinged usernames as options while creating profile
        if not obj:
            form.base_fields['user'].queryset = User.objects.filter(profile__isnull=True)
        return form
