from kpi_data import KPI_DATA

for kpi in KPI_DATA:
    if kpi.name == "open":
        print(F"Current Open tickets --> {kpi.value}")
    if kpi.name == "closed":
        print(F"Current Closed tickets --> {kpi.value}")
