from model_utils.models import TimeStampedModel, SoftDeletableModel


class BaseModel(TimeStampedModel, SoftDeletableModel):
    """
        This way I can access all the objects by saying MyModel.all_objects.all()
        MyModel.objects.all() will provide only the non soft deleted ones in both cases.
    """

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

