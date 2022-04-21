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
    )

    image_name = models.CharField(
        'Image Name',
        max_length=30,
    )

    region = models.CharField(
        'Region',
        max_length=30,
    )


class AccountID(models.Model):
    account_id = models.CharField(
        'Account ID',
        max_length=30,
    )
    pub_date = models.DateTimeField(
        'Date published'
    )

    def __str__(self):
        return self.account_id


class InstanceID(models.Model):
    instance_id = models.CharField(
        'Instance ID',
        max_length=30,
        primary_key=True,
    )

    def __str__(self):
        return self.instance_id


class ImageName(models.Model):
    image_name = models.CharField(
        'Image Name',
        max_length=30,
    )

    def __str__(self):
        return self.image_name


class Region(models.Model):
    region = models.CharField(
        'Region',
        max_length=30,
    )

    def __str__(self):
        return self.region

