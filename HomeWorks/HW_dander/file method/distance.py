from functools import total_ordering
from typing import Any

#### @total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам

    def __init__(self, other) -> None:
      pass
        
    def __eq__(self, value: object) -> bool:
        return hash(self)==hash(other)

      
    
    def as_millimeters(self) -> float:
        """Возвращает значение длины в миллиметах.

        :rtype: float
        :return: Значение округленное до 5 знаков после запятой
        """
        return round(self._value * self.ratio, 5)

class Centimeter(Millimeter):
    label = 'см'
    ratio = 10


class Meter(Millimeter):
    label = 'метр'
    ratio = 100


class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4
