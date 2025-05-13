# from django.core.mail import send_mail
# from django_cron import CronJobBase, Schedule
# from django.utils import timezone
# from datetime import timedelta
# from predictor.models import PlantGrowthRecord  # Assuming you have a model to track plant growth

# class SendWaterReminderCronJob(CronJobBase):
#     # Runs every day at 9 AM as set in CRONJOBS in settings.py
#     schedule = Schedule(run_every_mins=1440)  # 1440 minutes = 1 day
#     code = 'predictor.send_water_reminder'

#     def do(self):
#         # Fetch the plants that need watering (you could use more complex logic here)
#         plants_needing_water = PlantGrowthRecord.objects.filter(
#             last_watered__lt=timezone.now() - timedelta(days=2)
#         )

#         for plant in plants_needing_water:
#             # Send an email reminder (you can replace this with SMS or another notification service)
#             send_mail(
#                 '🌱 Water Your Plant!',
#                 f"Hi, it's time to water your plant {plant.name}. It hasn't been watered for more than 2 days.",
#                 'durgadevid2003@gmail.com',  # replace with your sender email
#                 [plant.user.email],  # send to the plant owner's email
#                 fail_silently=False,
#             )
