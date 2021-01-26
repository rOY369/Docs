from collections import namedtuple
from itertools import starmap

data = (("open", 10), ("closed", 20))
nt = namedtuple("KPI", "name value")
KPI_DATA = starmap(nt, data)
