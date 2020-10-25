#to created a profile instance everytime a user instance be created we used signals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Profile

#when an instance user be created, User class send a signal at post_save
#we will use the decorator receiver to take the signal from post_save
#the profile will created from decorator property

#User manda un segnale di crezione utente a post_save
#useremo il decoratore receiver per prendere il segnale da post_save
#creeremo il profilo in base al decoratore

#decorated the function with receiver that aspect the signal from post_save
#sender by User
#the created flag explain us, if the user instance is just to be created
#so the next step is to created the Profile user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("Created: ", created)
    if created:
        Profile.objects.create(user=instance)
        print(Profile.objects.all())
