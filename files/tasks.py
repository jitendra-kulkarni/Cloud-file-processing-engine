from celery import shared_task
from .models import File
from django.utils import timezone

@shared_task
def process_file(file_id):

    try:
        uploaded_file = File.objects.get(id=file_id)

        uploaded_file.status = "PROCESSING"
        uploaded_file.save(update_fields=["status"])

        uploaded_file.status = "COMPLETED"
        uploaded_file.processed_at = timezone.now()

        uploaded_file.save(
            update_fields=["status","processed_at"]
        )

    except File.DoesNotExist:
        print(f"File with id {file_id} does not exist.")

    except Exception as error:
        File.objects.filter(id=file_id).update(status="FAILED")

        raise error
