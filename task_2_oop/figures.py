from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class ColorCodes(Enum):
    WHITE = '#FFFFFF'
    BLACK = '#000000'
    RED = '#FF0000'


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int

    def print(self) -> str:
        return f'{self.x},{self.y}'


class DrawingFigure:
    def __init__(
        self,
        center_coordinates: Coordinates,
    ) -> None:
        self._color = ColorCodes.WHITE
        self._center_coordinates = center_coordinates

    @abstractmethod
    def draw(
        self,
    ) -> None:
        ...

    def set_color(
        self,
        color: ColorCodes,
    ) -> None:
        self._color = color


class Circle(DrawingFigure):
    def __init__(
        self,
        radius: float,
        center_coordinates: Coordinates,
    ) -> None:
        super().__init__(center_coordinates)
        self.__radius = radius

    def draw(
        self,
    ) -> None:
        logger.info(
            f'Drawing {self.__class__.__name__}.Center:{self._center_coordinates}.'
            f'Radius:{self.__radius}.Color:{self._color.value}'
        )


class Triangle(DrawingFigure):
    def __init__(self, base: float, height: float, center_coordinates: Coordinates) -> None:
        super().__init__(center_coordinates)
        self.__base = base
        self.__height = height

    def draw(self) -> None:
        logger.info(
            f'Drawing {self.__class__.__name__}.Color:{self._color.value}.Center:{self._center_coordinates}.'
            f'Base:{self.__base}.Height:{self.__height}'
        )


class Rectangle(DrawingFigure):
    def __init__(self, width: float, height: float, center_coordinates: Coordinates) -> None:
        super().__init__(center_coordinates)
        self.__width = width
        self.__height = height

    def draw(self) -> None:
        logger.info(
            f'Drawing {self.__class__.__name__}.Color:{self._color.value}.Center:{self._center_coordinates}.'
            f'Base:{self.__width}.Height:{self.__height}'
        )
