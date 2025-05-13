# from django.db import models
# from django.contrib.auth.models import User
 

# # Create a user with email
# # user = User.objects.create_user(username="john_doe", password="password123", email="john@example.com")

# class PlantGrowthRecord(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User model
#     last_watered = models.DateTimeField(auto_now=True)
#     growth_rate = models.CharField(max_length=20, choices=[('slow', 'Slow'), ('moderate', 'Moderate'), ('fast', 'Fast')])

#     def __str__(self):
#         return self.name

