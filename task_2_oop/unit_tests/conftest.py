import logging

import pytest

from task_2_oop.engine_2d import Canvas, Engine2D
from task_2_oop.figures import Circle, Coordinates, Rectangle, Triangle

logging.basicConfig(handlers=[
    logging.StreamHandler()
],
    level=logging.INFO)


@pytest.fixture
def canvas() -> Canvas:
    return Canvas()


@pytest.fixture
def engine_2d() -> Engine2D:
    return Engine2D()


@pytest.fixture
def circle() -> Circle:
    return Circle(5.0, Coordinates(0, 0))


@pytest.fixture
def triangle() -> Triangle:
    return Triangle(5.0, 3.0, Coordinates(5, 5))


@pytest.fixture
def rectangle() -> Rectangle:
    return Rectangle(4.0, 6.0, Coordinates(10, 10))
