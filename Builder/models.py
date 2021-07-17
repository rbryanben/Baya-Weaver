from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# path for each user
def user_dir(instance, filename):
    return 'user_{0}{1}'.format(instance.user.id, filename)


class Theme(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    theme_name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to=user_dir, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class EditorialChanges(models.Model):
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    pallet_top = models.IntegerField()
    pallet_mid = models.IntegerField()
    pallet_bottom = models.IntegerField()