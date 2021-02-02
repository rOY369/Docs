from kpis import KPIS
from kpis_dashboard import Dashboard

kpis = KPIS()
dashboard = Dashboard(kpis)

kpis.set_kpis(10, 20)

kpis.set_kpis(14, 30)

kpis.set_kpis(2, 6)

kpis.detach(dashboard)

kpis.set_kpis(9, 9)

kpis.attach(dashboard)

kpis.set_kpis(19, 9)
