from django.contrib import admin

from solo_prep.web.models import Profile, Album


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    pass