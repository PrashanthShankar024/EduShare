from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.db import models
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

from .forms import MaterialForm, ReviewForm
from .models import Material, Bookmark, Review

@login_required
def upload_material(request):

    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            material = form.save(
                commit=False
            )

            material.uploaded_by = request.user

            material.save()

            return redirect('home')

    else:

        form = MaterialForm()

    return render(
        request,
        'materials/upload.html',
        {
            'form': form
        }
    )


def material_list(request):

    materials = Material.objects.annotate(
    average_rating=Avg('reviews__rating')
).order_by('-uploaded_at')

    # Search
    search_query = request.GET.get('search', '')

    if search_query:
        materials = materials.filter(
            models.Q(title__icontains=search_query)
            | models.Q(subject__icontains=search_query)
            | models.Q(description__icontains=search_query)
        )

    # Semester filter
    semester = request.GET.get('semester', '')

    if semester:
        materials = materials.filter(
            semester=semester
        )

    # Resource type filter
    resource_type = request.GET.get(
        'resource_type',
        ''
    )

    if resource_type:
        materials = materials.filter(
            resource_type=resource_type
        )

    return render(
        request,
        'materials/material_list.html',
        {
            'materials': materials,
            'search_query': search_query,
            'selected_semester': semester,
            'selected_resource_type': resource_type,
        }
    )
    
    
def material_detail(request, pk):
    material = get_object_or_404(
        Material,
        pk=pk
    )

    is_bookmarked = False

    if request.user.is_authenticated:
        is_bookmarked = Bookmark.objects.filter(
            user=request.user,
            material=material
        ).exists()

    reviews = Review.objects.filter(
        material=material
    ).select_related(
        'user'
    ).order_by(
        '-created_at'
    )

    review_form = ReviewForm()

    rating_data = reviews.aggregate(
        average_rating=Avg('rating')
    )

    average_rating = rating_data['average_rating']

    return render(
        request,
        'materials/material_detail.html',
        {
            'material': material,
            'is_bookmarked': is_bookmarked,
            'reviews': reviews,
            'review_form': review_form,
            'average_rating': average_rating,
        }
    )
       
@login_required
def edit_material(request, pk):

    material = get_object_or_404(
        Material,
        pk=pk,
        uploaded_by=request.user
    )

    if request.method == 'POST':

        form = MaterialForm(
            request.POST,
            request.FILES,
            instance=material
        )

        if form.is_valid():

            form.save()

            return redirect(
                'material_detail',
                pk=material.pk
            )

    else:

        form = MaterialForm(
            instance=material
        )

    return render(
        request,
        'materials/edit_material.html',
        {
            'form': form,
            'material': material
        }
    )


@login_required
def delete_material(request, pk):

    material = get_object_or_404(
        Material,
        pk=pk,
        uploaded_by=request.user
    )

    if request.method == 'POST':

        material.delete()

        return redirect('dashboard')

    return render(
        request,
        'materials/delete_material.html',
        {
            'material': material
        }
    )
    
@login_required
def add_bookmark(request, pk):

    material = get_object_or_404(
        Material,
        pk=pk
    )

    Bookmark.objects.get_or_create(
        user=request.user,
        material=material
    )

    return redirect(
        'material_detail',
        pk=material.pk
    )
    
@login_required
def remove_bookmark(request, pk):

    material = get_object_or_404(
        Material,
        pk=pk
    )

    Bookmark.objects.filter(
        user=request.user,
        material=material
    ).delete()

    return redirect(
        'material_detail',
        pk=material.pk
    )
    
@login_required
def add_review(request, pk):
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.material = material
            review.save()

    return redirect('material_detail', pk=material.pk)


@login_required
def delete_review(request, pk):
    review = get_object_or_404(
        Review,
        pk=pk,
        user=request.user
    )

    material_pk = review.material.pk

    if request.method == 'POST':
        review.delete()

    return redirect(
        'material_detail',
        pk=material_pk
    )