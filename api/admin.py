from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from .models import Donation
from .models import Expense

admin.site.site_header = 'Helping Hands Administration'
admin.site.index_title = 'Helping Hands'
admin.site.site_title = 'Administration'



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'phone', 'email', 'blood_group', 'address', 'photo')
    list_display = ('name', 'phone', 'email', 'address', )
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
        if not obj:
            form.base_fields['collector'].queryset = User.objects.filter(is_staff=True, is_superuser=False)
        return form


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    date_hierarchy = 'spent_at'
    fields = ('spender', 'amount', 'reference', 'spent_at', )
    list_display = ('spender', 'amount', 'reference', 'spent_at', 'logged_at')
    list_display_links = None

    def get_form(self, request, obj=None, **kwargs):
        form = super(ExpenseAdmin, self).get_form(request, obj, **kwargs)
        if not obj:
            form.base_fields['spender'].queryset = Profile.objects.filter(user__id=request.user.id, user__is_staff=True, user__is_superuser=True)
        return form

    def has_change_permission(self, request, obj=None):
        return False
