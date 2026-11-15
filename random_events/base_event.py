from abc import ABC, abstractmethod

class RandomEvent(ABC):
    """
    Базовый класс для всех случайных событий в игре.
    """
    @abstractmethod
    def execute(self, engine):
        """
        Метод, который запускает событие.
        engine: Ссылка на игровой движок GameEngine (чтобы менять стейты или получать героя).
        """
        pass

    def get_weight(self, hero):
        """
        Метод для получения веса события. По умолчанию возвращает 0.5.
        """
        return 0.5
