from abc import ABC, abstractmethod
from time import perf_counter

from .asset_cache import AssetCache

from datetime import timedelta

asset_cache = AssetCache()
endpoints = {}

buckets = {}


class Endpoint(ABC):
    def __init__(self):
        pass

    @property
    def name(self):
        return self.__class__.__name__.lower()

    @property
    def bucket(self):
        return buckets.get(self.name)

    def get_avg_gen_time(self):
        if self.avg_generation_times.len() == 0:
            return 0

        return round(self.avg_generation_times.sum(), 2)

    def run(self, key, **kwargs):
        res = self.generate(**kwargs)
        return res

    @abstractmethod
    def generate(self, avatars, text, usernames, kwargs):
        raise NotImplementedError(
            f"generate has not been implemented on endpoint {self.name}"
        )


def setup(klass=None, rate=5, per=1):
    if klass:
        kls = klass()
        endpoints[kls.name] = kls
        return kls
    else:

        def wrapper(klass, *a, **ka):
            kls = klass()
            endpoints[kls.name] = kls
            return kls

        return wrapper
