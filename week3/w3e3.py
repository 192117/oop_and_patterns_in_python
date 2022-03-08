from abc import ABC, abstractmethod

class ObservableEngine(Engine):

    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscribe):
        self.__subscribers.add(subscribe)

    def unsubscribe(self, subscribe):
        self.__subscribers.remove(subscribe)

    def notify(self, achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement["title"])


class FullNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)