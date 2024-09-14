import pandas as pd
import punq

from data import load_dataset
from service import SalesService


def get_container() -> punq.Container:
    container = punq.Container()

    container.register(SalesService, scope=punq.Scope.singleton)

    container.register(pd.DataFrame, load_dataset, scope=punq.Scope.singleton)

    return container
