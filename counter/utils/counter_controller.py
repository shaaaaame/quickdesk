from django.utils import timezone

from .queue import Queue
from ..models import Ticket, Counter

class CounterController:

    def __init__(self):
        self._ticket_queue = Queue()
        self._latest_serving_num = 0
        self._last_issued_num = 0
        self.counters = Counter.objects.all()

        ticket_list = list(Ticket.objects.filter(complete=False))
        for ticket in ticket_list:
            self._ticket_queue.enqueue(ticket)
        
        self.resetCounters()

    def resetCounters(self):
        for counter in self.counters:
            counter.setOnline()
            counter.cur_num = None
            counter.save()
        
    def getCounterData(self):
        return {
            'counters': self.counters,
            'latest_serving_num': self._latest_serving_num,
            'last_issued_num': self._last_issued_num
        }

    def takeTicket(self) -> Ticket:
        self._last_issued_num += 1
        ticket = Ticket(ticket_number=self._last_issued_num, date_issued=timezone.now())
        ticket.save()
        self._ticket_queue.enqueue(ticket)

        print("Issued ticket: ", ticket.ticket_number)
        return ticket

    def serveTicket(self) -> Ticket:
        next_ticket = self._ticket_queue.dequeue()
        if next_ticket is None:
            return None
        self._latest_serving_num = next_ticket.ticket_number

        return next_ticket        
