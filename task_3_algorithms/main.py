from dataclasses import dataclass
import logging
from typing import List

import click

from task_3_algorithms.breadth_first_search_algorithm import BreadthFirstSearchAlgorithm
from task_3_algorithms.map import MapGenerator

logging.basicConfig(handlers=[
    logging.StreamHandler()
],
    level=logging.INFO)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class InputData:
    grid: List[List[str]]
    point_start: Point
    point_end: Point


@click.command()
@click.option('--grid_rows', type=int, default=10, help='Number of rows')
@click.option('--grid_columns', type=int, default=10, help='Number of columns')
@click.option('--start-x', type=int, default=1, help='X-coordinate of the start point')
@click.option('--start-y', type=int, default=1, help='Y-coordinate of the start point')
@click.option('--end-x', type=int, default=3, help='X-coordinate of the end point')
@click.option('--end-y', type=int, default=4, help='Y-coordinate of the end point')
def main(
    grid_rows: int,
    grid_columns: int,
    start_x: int,
    start_y: int,
    end_x: int,
    end_y: int
):
    generated_map = MapGenerator.generate(grid_rows, grid_columns)
    # Assuming that the start and final points are 'W' to prevent the boatman from hitting land.
    generated_map[start_x][start_y] = 'W'
    generated_map[end_x][end_y] = 'W'
    print_map(generated_map)
    list_of_points, steps = BreadthFirstSearchAlgorithm.get_shortest_path(
        proposed_map=generated_map,
        start_point=(start_x, start_y),
        end_point=(end_x, end_y),
        block_value='E',
    )
    for step_point in list_of_points:
        generated_map[step_point[0]][step_point[1]] = '▲'
    print_map(generated_map)
    logger.info(f"The shortest path length is: {steps}")


def print_map(
    map_for_print: List[List[str]],
) -> None:
    logger.info('Show the map. Point 0,0 - top left corner.')
    for col in range(len(map_for_print[0])):
        column_data = [map_for_print[row][col] for row in range(len(map_for_print))]
        logger.info(column_data)


if __name__ == "__main__":
    main()
