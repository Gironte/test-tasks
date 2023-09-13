import threading
from unittest.mock import Mock

import pytest

from task_2_oop.engine_2d import Engine2D
from task_2_oop.figures import Circle, ColorCodes, Coordinates, Rectangle, Triangle


class TestEngine:
    def test_engine_add_new_element_success(self, engine_2d: Engine2D, circle: Circle) -> None:
        engine_2d.set_default_color(ColorCodes.RED)
        engine_2d.add_new_element(circle)
        assert engine_2d.get_canvas_elements_count() == 1

    def test_engine_add_new_element_without_color_catch_error(self, engine_2d: Engine2D, circle: Circle) -> None:
        with pytest.raises(ValueError):
            engine_2d.add_new_element(circle)

    def test_engine_draw_and_clear_success(
        self,
        engine_2d: Engine2D,
        circle: Circle,
        triangle: Triangle,
        rectangle: Rectangle
    ) -> None:
        engine_2d.set_default_color(ColorCodes.RED)
        engine_2d.add_new_element(circle)
        engine_2d.add_new_element(triangle)
        engine_2d.add_new_element(rectangle)
        assert engine_2d.get_canvas_elements_count() > 0
        engine_2d.draw()
        assert engine_2d.get_canvas_elements_count() == 0

    def test_engine_multi_thread_draw(self, engine_2d: Engine2D) -> None:
        engine_2d.set_default_color(ColorCodes.RED)
        for _ in range(100):
            circle = Circle(5.0, Coordinates(0, 0))
            engine_2d.add_new_element(circle)

        assert engine_2d.get_canvas_elements_count() == 100

        def worker():
            engine_2d.draw()

        threads = []
        for _ in range(10):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        assert engine_2d.get_canvas_elements_count() == 0

    def test_circle_draw_success(self, circle: Circle) -> None:
        circle.draw = Mock()
        circle.draw()
        circle.draw.assert_called()

    def test_rectangle_draw_success(self, rectangle: Rectangle) -> None:
        rectangle.draw = Mock()
        rectangle.draw()
        rectangle.draw.assert_called()

    def test_triangle_draw_success(self, triangle: Triangle) -> None:
        triangle.draw = Mock()
        triangle.draw()
        triangle.draw.assert_called()
