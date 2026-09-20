from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):

    # Resource type choices
    RESOURCE_TYPES = [
        ('pdf', 'PDF'),
        ('document', 'Document'),
        ('presentation', 'Presentation'),
        ('spreadsheet', 'Spreadsheet'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('archive', 'Archive'),
        ('other', 'Other'),
    ]

    # Semester choices
    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'),
        ('7', '7th Semester'),
        ('8', '8th Semester'),
    ]

    # Basic information
    title = models.CharField(max_length=200)

    description = models.TextField()

    subject = models.CharField(max_length=100)

    # Academic semester
    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES
    )

    # Type of resource
    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPES,
        default='other'
    )

    # Uploaded file
    resource_file = models.FileField(
        upload_to='resources/'
    )

    # User who uploaded the resource
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Automatically stores upload date and time
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class Bookmark(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'material'],
                name='unique_user_material_bookmark'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.material.title}"
    
    
class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'material'],
                name='unique_user_material_review'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.material.title} - {self.rating}"