from django.db import models
from django.contrib.auth.models import User



# Industry model
class Industries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    @property
    def name_length(self):
        return len(self.name)
    
# Company model
class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industries = models.ManyToManyField(Industries, related_name='companies')

    def __str__(self):
        return self.name

# JobPost model
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Review model
class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.company} ({self.rating}/5)'
    
    @property
    def review_length(self):
        return len(self.comment)

# Application model
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} applied for {self.job_post}'

