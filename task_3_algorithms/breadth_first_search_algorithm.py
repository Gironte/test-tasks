from collections import deque
from typing import List, Tuple


class BreadthFirstSearchAlgorithm:
    @staticmethod
    def get_shortest_path(
        proposed_map: List[List[str]],
        start_point: Tuple[int, int],
        end_point: Tuple[int, int],
        block_value: str,
    ) -> Tuple[List, int]:
        parent = {}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(proposed_map), len(proposed_map[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = deque([(start_point, 0)])
        while queue:
            (x, y), steps = queue.popleft()
            if (x, y) == end_point:
                path = [(x, y)]
                while (x, y) != start_point:
                    x, y = parent[(x, y)]
                    path.append((x, y))
                return list(reversed(path)), steps
            if visited[x][y] or proposed_map[x][y] == block_value:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                next_step_x, next_step_y = x + dx, y + dy
                if 0 <= next_step_x < rows and 0 <= next_step_y < cols and not visited[next_step_x][next_step_y]:
                    parent[(next_step_x, next_step_y)] = (x, y)
                    queue.append(((next_step_x, next_step_y), steps + 1))
        raise ValueError(f'There is no path from {start_point} to point {end_point}')
