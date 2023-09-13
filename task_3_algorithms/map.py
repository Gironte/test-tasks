import logging
import random
from typing import List

logger = logging.getLogger(__name__)


class MapGenerator:
    @staticmethod
    def generate(
        length: int,
        width: int,
        percentage_e=0.3,
    ) -> List[List[str]]:
        result_map = []
        total_cells_count = length * width
        earth_cells_count = int(total_cells_count * percentage_e)
        flat_array = ['E'] * earth_cells_count + ['W'] * (total_cells_count - earth_cells_count)
        random.shuffle(flat_array)
        for item_length in range(length):
            map_row = []
            for item_width in range(width):
                map_row.append(flat_array.pop())
            result_map.append(map_row)
        return result_map
