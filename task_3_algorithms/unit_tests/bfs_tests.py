from typing import List, Tuple

import pytest

from task_3_algorithms.breadth_first_search_algorithm import BreadthFirstSearchAlgorithm


class TestsBfsAlgorithm:
    @pytest.mark.parametrize(
        'proposed_map, start_point, end_point, block_value, expected_path, expected_steps',
        [
            (
                [
                    ['W', 'W', 'W'],
                    ['W', 'W', 'W'],
                    ['W', 'W', 'W']
                ],
                (0, 0),
                (2, 2),
                'X',
                [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                4
            ),
            (
                [
                    ['W', 'W', 'W'],
                    ['W', '#', 'W'],
                    ['W', 'W', 'W']
                ],
                (0, 0),
                (2, 2),
                '#',
                [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
                4
            ),
        ]
    )
    def test_get_shortest_path_success(
        self,
        proposed_map,
        start_point,
        end_point,
        block_value,
        expected_path: List[Tuple[int, int]],
        expected_steps: int,
    ) -> None:
        path, steps = BreadthFirstSearchAlgorithm.get_shortest_path(
            proposed_map, start_point, end_point, block_value
        )
        assert path == expected_path
        assert steps == expected_steps

    def test_get_shortest_path_no_path_error_received(self) -> None:
        proposed_map = [
            ['W', 'X', 'W'],
            ['X', 'W', 'X'],
            ['W', 'X', 'W']
        ]
        start_point = (0, 0)
        end_point = (2, 2)
        block_value = 'X'
        with pytest.raises(ValueError):
            BreadthFirstSearchAlgorithm.get_shortest_path(
                proposed_map, start_point, end_point, block_value
            )

    def _create_map(self, rows, cols, block_value) -> List[List[str]]:
        return [[block_value] * cols for _ in range(rows)]

    def _print_map(self, proposed_map) -> None:
        for row in proposed_map:
            print(''.join(row))
