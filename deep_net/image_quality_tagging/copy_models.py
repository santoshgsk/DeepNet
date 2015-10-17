from django.contrib.gis.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

#    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

# class FlatImages(models.Model):
#     id = models.AutoField(primary_key=True)
#     flat_id = models.IntegerField()
#     service = models.CharField(max_length=50)
#     image_name = models.CharField(max_length=255)
#     image_encoded = models.CharField(max_length=255)
#     num_user_tags = models.IntegerField(db_index=True, default=0)
#
#     class Meta:
#         unique_together = ("flat_id", "image_encoded")
#         app_label = 'image_quality_tagging'
#
#
# class FlatImageTag(models.Model):
#     id = models.AutoField(primary_key=True)
#     uid = models.CharField(max_length=50)
#     flat_id = models.IntegerField()
#     image_encoded = models.CharField(max_length=255)
#     img_wall = models.IntegerField(null=True)
#     img_cleanliness = models.IntegerField(null=True)
#     img_spacious = models.IntegerField(null=True)
#     img_flat_overall = models.IntegerField(null=True)
#     img_windows_size = models.IntegerField(null=True)
#
#     class Meta:
#         unique_together = ("uid", "image_encoded")
#         index_together = [
#             ['uid', 'image_encoded']
#         ]
#         app_label = 'image_quality_tagging'
