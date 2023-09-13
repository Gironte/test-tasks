import logging

from task_2_oop.engine_2d import Engine2D
from task_2_oop.figures import ColorCodes, Coordinates, Rectangle

logging.basicConfig(handlers=[
    logging.StreamHandler()
],
    level=logging.INFO)

logger = logging.getLogger(__name__)

engine = Engine2D()

engine.set_default_color(ColorCodes.BLACK)
engine.add_new_element(Rectangle(4.0, 4.3, Coordinates(2, 3)))
engine.add_new_element(Rectangle(4.0, 4.3, Coordinates(2, 3)))
engine.add_new_element(Rectangle(4.0, 4.3, Coordinates(2, 3)))
engine.set_default_color(ColorCodes.RED)
engine.add_new_element(Rectangle(4.0, 4.3, Coordinates(2, 3)))
engine.add_new_element(Rectangle(4.0, 4.3, Coordinates(2, 3)))

engine.draw()
