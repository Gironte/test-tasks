import logging
from queue import Queue
from threading import Lock

from task_2_oop.figures import ColorCodes, DrawingFigure

logger = logging.getLogger(__name__)


class Canvas:
    def __init__(self) -> None:
        self.__queue = Queue()

    def add_new_element(self, figure: DrawingFigure) -> None:
        self.__queue.put(figure)

    def get_last_element(self) -> DrawingFigure:
        return self.__queue.get(block=False)

    def is_empty(self) -> bool:
        return self.__queue.empty()

    def get_elements_count(self) -> int:
        return self.__queue.qsize()


class Engine2D:
    __lock = Lock()

    def __init__(self):
        self.__canvas = Canvas()
        self.__default_color = None

    def add_new_element(self, figure: DrawingFigure) -> None:
        if not self.__default_color:
            raise ValueError('Set default color')
        figure.set_color(self.__default_color)
        self.__canvas.add_new_element(figure)

    def draw(self) -> None:
        while not self.__canvas.is_empty():
            self.__canvas.get_last_element().draw()

    def set_default_color(self, color: ColorCodes) -> None:
        self.__default_color = color

    def get_canvas_elements_count(self) -> int:
        return self.__canvas.get_elements_count()
