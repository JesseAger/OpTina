from django.db import models
from users.models import CustomUser

class tickets(models.Model):
    STATUS_CHOICES =(
        ('PENDING', "Pending"),
        ('UNDER REVIEW', "Under Review"),
        ('SOLVED', "Under Review")
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    ticket_number = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    title = models.CharField(max_length=100)
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name= 'reported_tickets')
    assigned_to =  models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_tickets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class TicketComment(models.Model):
    ticket = models.ForeignKey(tickets, on_delete=models.SET_NULL, blank=True, null= True, related_name='comment')
    author = models. ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp =  models.DateTimeField(auto_now_add=True)
    

