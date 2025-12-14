from django.db import models

class Bucket(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Object(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    file = models.FileField(upload_to='buckets/')
    key = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.file.name = f"{self.bucket.name}/{self.key}"
        super().save(*args, **kwargs)
