from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from materials.models import Material, Bookmark, Review

def home(request):
    from django.contrib.auth.models import User

    total_resources = Material.objects.count()
    total_users = User.objects.count()
    total_reviews = Review.objects.count()

    latest_materials = Material.objects.order_by(
        '-uploaded_at'
    )[:6]

    return render(
        request,
        'core/home.html',
        {
            'total_resources': total_resources,
            'total_users': total_users,
            'total_reviews': total_reviews,
            'latest_materials': latest_materials,
        }
    )


@login_required
def dashboard(request):

    user = request.user

    materials = Material.objects.filter(
        uploaded_by=user
    ).order_by('-uploaded_at')

    total_uploads = materials.count()

    return render(
        request,
        'core/dashboard.html',
        {
            'materials': materials,
            'total_uploads': total_uploads,
        }
    )
    
@login_required
def bookmarks(request):

    bookmarks = Bookmark.objects.filter(
        user=request.user
    ).select_related(
        'material'
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'core/bookmarks.html',
        {
            'bookmarks': bookmarks
        }
    )
    
@login_required
def profile(request):
    user = request.user

    total_uploads = Material.objects.filter(
        uploaded_by=user
    ).count()

    total_bookmarks = Bookmark.objects.filter(
        user=user
    ).count()

    total_reviews = Review.objects.filter(
        user=user
    ).count()

    return render(
        request,
        'core/profile.html',
        {
            'total_uploads': total_uploads,
            'total_bookmarks': total_bookmarks,
            'total_reviews': total_reviews,
        }
    )