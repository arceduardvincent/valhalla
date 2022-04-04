from django.db import models


class AWSVirtualMachine(models.Model):
    account_id = models.CharField(
        'Account ID',
        max_length=30,
    )

    instance_id = models.CharField(
        'Instance ID',
        max_length=30,
        primary_key=True,
        editable=False,
    )

    image_name = models.CharField(
        'Image Name',
        max_length=30,
    )

    region = models.CharField(
        'Region',
        max_length=30,
    )
