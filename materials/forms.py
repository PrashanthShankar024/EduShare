from django import forms
from .models import Material, Review


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material

        fields = [
            'title',
            'description',
            'subject',
            'semester',
            'resource_type',
            'resource_file',
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Enter resource title'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe this resource',
                    'rows': 5
                }
            ),

            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Example: Python'
                }
            ),

            'semester': forms.Select(),

            'resource_type': forms.Select(),
        }

    def clean_resource_file(self):

        file = self.cleaned_data.get('resource_file')

        if not file:
            raise forms.ValidationError(
                'Please select a file.'
            )

        # Maximum file size: 100 MB
        max_size = 100 * 1024 * 1024

        if file.size > max_size:
            raise forms.ValidationError(
                'File size cannot exceed 100 MB.'
            )

        # Allowed extensions
        allowed_extensions = [
            '.pdf',

            '.doc',
            '.docx',

            '.ppt',
            '.pptx',

            '.xls',
            '.xlsx',

            '.jpg',
            '.jpeg',
            '.png',
            '.gif',
            '.webp',

            '.mp4',
            '.webm',
            '.mov',

            '.zip',
        ]

        file_name = file.name.lower()

        if not any(
            file_name.endswith(ext)
            for ext in allowed_extensions
        ):
            raise forms.ValidationError(
                'This file type is not allowed.'
            )

        return file
    
    
class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment']

        widgets = {
            'rating': forms.Select(
                choices=[
                    (1, '⭐ 1 - Poor'),
                    (2, '⭐⭐ 2 - Fair'),
                    (3, '⭐⭐⭐ 3 - Good'),
                    (4, '⭐⭐⭐⭐ 4 - Very Good'),
                    (5, '⭐⭐⭐⭐⭐ 5 - Excellent'),
                ]
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Write your review...',
                    'rows': 4
                }
            ),
        }