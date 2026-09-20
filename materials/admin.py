from django.contrib import admin
from .models import Material, Bookmark, Review

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'subject',
        'semester',
        'resource_type',
        'uploaded_by',
        'uploaded_at',
    )

    list_filter = (
        'resource_type',
        'semester',
        'subject',
        'uploaded_at',
    )

    search_fields = (
        'title',
        'subject',
        'description',
    )

    ordering = (
        '-uploaded_at',
    )
    
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'material',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'user__username',
        'material__title',
    )
    
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'material',
        'rating',
        'created_at',
    )

    list_filter = (
        'rating',
        'created_at',
    )

    search_fields = (
        'user__username',
        'material__title',
        'comment',
    )

    ordering = ('-created_at',)