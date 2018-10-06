from django.db import models

# Create your models here.



class users_profiles(models.Model):
    username=models.CharField(max_length=30,blank=False)
    useremail=models.EmailField(max_length=30,blank=False)
    password=models.CharField(max_length=30,blank=False)


class input_quote(models.Model):
    text = models.CharField(max_length=500)
    sayer = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True,null=False)


class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email    