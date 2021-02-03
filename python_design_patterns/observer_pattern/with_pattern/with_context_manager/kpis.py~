from abstract_subject import AbstractSubject


class KPIS(AbstractSubject):

    _openTickets = -1
    _closedTickets = -1

    @property
    def open_tickets(self):
        return self._openTickets

    @property
    def closed_tickets(self):
        return self._closedTickets

    def set_kpis(self, openTickets, closedTickets):
        self._openTickets = openTickets
        self._closedTickets = closedTickets
        self.notify()
