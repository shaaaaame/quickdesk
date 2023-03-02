from django.shortcuts import render

from .models import Counter, Ticket
from .utils.queue import Queue
from .utils.counter_controller import CounterController

counter_controller = CounterController() # change where this is instantiated
customer_ticket = None

def index(request):
        return render(request, 'index.html')

def counter(request):
    global counter_controller
    controller_data = counter_controller.getCounterData()
    counters = controller_data['counters']
    context = {'counters': counters}

    if request.method == 'POST':
        data = request.POST
        print(data)
        if data.get('offline'):
            counter = counters[int(data.get('offline'))- 1]
            counter.setOffline()
            counter.save()
        elif data.get('online'):
            counter = counters[int(data.get('online'))- 1]
            counter.setOnline()
            counter.save()
        elif data.get('complete'):
            counter = counters[int(data.get('complete'))- 1]
            counter.completeCur()
            counter.save()
        elif data.get('next'):
            counter = counters[int(data.get('next'))- 1]
            next_ticket = counter_controller.serveTicket()
            counter.callNext(next_ticket.ticket_number)
            counter.save()

    return render(request, 'counter.html', context)

def customer(request):
    global customer_ticket
    global counter_controller

    context = counter_controller.getCounterData()
    context['customer_ticket'] = customer_ticket
    if request.method == 'POST':
        customer_ticket = counter_controller.takeTicket()
        context = counter_controller.getCounterData()
        context['customer_ticket'] = customer_ticket
        customer_ticket.save()

    return render(request, 'customer.html', context)

