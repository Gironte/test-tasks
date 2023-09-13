from queue import Empty
import threading

import pytest

from task_2_oop.engine_2d import Canvas
from task_2_oop.figures import Circle, Coordinates


class TestsCanvas:
    def test_canvas_add_new_element_success(self, canvas: Canvas, circle: Circle) -> None:
        canvas.add_new_element(circle)
        assert canvas.get_elements_count() == 1
        assert not canvas.is_empty()

    def test_canvas_get_last_element_success(self, canvas: Canvas) -> None:
        circle = Circle(5.0, Coordinates(0, 0))
        canvas.add_new_element(circle)
        element = canvas.get_last_element()
        assert isinstance(element, Circle)
        assert element == circle

    def test_canvas_get_last_element_if_empty_catch_error(self, canvas: Canvas) -> None:
        with pytest.raises(Empty):
            canvas.get_last_element()

    def test_canvas_multi_thread_get_last_element_success(self, canvas: Canvas) -> None:
        for _ in range(100):
            circle = Circle(5.0, Coordinates(0, 0))
            canvas.add_new_element(circle)

        assert canvas.get_elements_count() == 100

        def worker():
            while True:
                try:
                    canvas.get_last_element()
                except Empty:
                    break

        threads = []
        for _ in range(10):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        assert canvas.get_elements_count() == 0
