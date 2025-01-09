from abc import ABC, abstractmethod

class LocationPoint(ABC):
    @abstractmethod
    def get_latitude(self):
        pass

    @abstractmethod
    def get_longitude(self):
        pass

class SearchablePoint(LocationPoint):

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude