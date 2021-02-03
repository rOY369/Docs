from kpis import KPIS
from kpis_dashboard import Dashboard

with KPIS() as kpis:
    with Dashboard(kpis):

        kpis.set_kpis(10, 20)

        kpis.set_kpis(14, 30)

        kpis.set_kpis(2, 6)

kpis.set_kpis(9, 9)
