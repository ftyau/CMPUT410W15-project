from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    uuid = models.CharField(max_length=32, default = uuid.uuid4)
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'))

    user = models.OneToOneField(User, editable=False)
    host = models.CharField(max_length=32, blank=True)
    displayname = models.CharField(max_length=128, blank=True)
    body = models.TextField(max_length=2048, blank=True)
    birthdate = models.DateField('birthdate',null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='profile_images', blank=True)
    workspace = models.CharField(max_length=128, blank=True)
    school = models.CharField(max_length=128, blank=True)
    follows = models.ManyToManyField('self', blank=True, symmetrical=False, through='Follow')
    friends = models.ManyToManyField('self', blank=True)

    @classmethod
    def create_profile(cls, username):
        profile = cls(user=username)
        profile.save()
        return profile

    def __unicode__(self):
        return str(self.user)

class Follow(models.Model):
    STATUS = (('REJECTED', 'Rejected'),
            ('PENDING', 'Pending'),
    )
    
    from_profile_id = models.ForeignKey(Profile, related_name='from_profile_id')
    to_profile_id = models.ForeignKey(Profile, related_name='to_profile_id')
    status = models.CharField(max_length=10, choices=STATUS)
