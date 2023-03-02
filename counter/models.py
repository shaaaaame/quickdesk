from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket_number = models.IntegerField(default=0, primary_key=True)
    complete = models.BooleanField(default=False)
    date_issued = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ticket_number)
    
class Counter(models.Model):
    cur_num = models.IntegerField(default=0, null=True)
    counter_number = models.SmallIntegerField(primary_key=True)
    is_online = models.BooleanField(default=True)

    def setOffline(self):
        self.is_online = False

    def setOnline(self):
        self.is_online = True

    def completeCur(self):
        Ticket.objects.filter(ticket_number=self.cur_num).update(complete=True)
        self.cur_num = None

    def callNext(self, next_num):
        self.cur_num = next_num
