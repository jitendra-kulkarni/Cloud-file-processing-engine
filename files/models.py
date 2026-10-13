from django.db import models

# Create your models here.

class File(models.Model):

    STATUS_CHOISES=[
        ('UPLOADED', 'uploaded'),
        ('PROCESSING', 'processing'),
        ('COMPLETED','completed'),
        ('FAILED','failed'),
    ]

    original_name = models.CharField(max_length=100)

    file = models.FileField(upload_to="upload/")

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOISES,
        default="UPLOADED",
    )

    uploaded_at=models.DateTimeField(auto_now_add=True)

    processed_at= models.DateTimeField(
        null=True, 
        blank=True,
    )

    def __str__(self):
        return self.original_name