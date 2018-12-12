from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from .models import Donation

admin.site.site_header = 'Helping Hands Administration'
admin.site.index_title = 'Helping Hands'
admin.site.site_title = 'Administration'



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'phone', 'email', 'address', 'photo')
    list_display = ('first_name', 'last_name', 'phone', 'email', 'address', )
    list_filter = []

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProfileAdmin, self).get_form(request, obj, **kwargs)
        # Show only unassinged usernames as options while creating profile
        if not obj:
            form.base_fields['user'].queryset = User.objects.filter(profile__isnull=True)
        return form


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    date_hierarchy = 'collected_at'
    fields = ('donor', 'amount', 'collector', 'collected_at', )
    list_display = ('donor', 'amount', 'collected_at', 'logged_at', 'collector')
    list_filter = ['collector']

    def get_form(self, request, obj=None, **kwargs):
        form = super(DonationAdmin, self).get_form(request, obj, **kwargs)
        # Show only unassinged usernames as options while creating profile
        if not obj:
            form.base_fields['collector'].queryset = User.objects.filter(is_staff=True, is_superuser=False)
        return form
    # pass