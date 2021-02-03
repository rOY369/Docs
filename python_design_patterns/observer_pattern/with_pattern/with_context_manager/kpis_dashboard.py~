from abstract_observer import AbstractObserver


class Dashboard(AbstractObserver):

    _openTickets = -1
    _closedTickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        self._kpis.attach(self)

    def update(self):
        self._openTickets = self._kpis.open_tickets
        self._closedTickets = self._kpis.closed_tickets
        self.display()

    def display(self):
        print("SIMPLE DASHBOARD DISPLAY")
        print(F"OPEN TICKETS ----> {self._openTickets}")
        print(F"CLOSED TICKETS ----> {self._closedTickets}")
        print("***DISPLAY OFF***\n")
