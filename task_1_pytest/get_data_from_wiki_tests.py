from typing import List

from _pytest.fixtures import FixtureRequest
import pytest

from task_1_pytest.wikipedia_client import ProgrammingLanguagesStatisticEntity, WikipediaClient, WikipediaRepository

test_data = [
    10 ** 7,
    int(1.5 * (10 ** 7)),
    5 * 10 ** 7,
    10 ** 8,
    5 * 10 ** 8,
    10 ** 9,
    int(1.5 * 10 ** 9)
]


@pytest.fixture(scope='session', params=test_data)
def get_test_data(request: FixtureRequest) -> int:
    return request.param


@pytest.fixture(scope='session')
def wikipedia_client() -> WikipediaClient:
    return WikipediaClient()


@pytest.fixture(scope='session')
def wikipedia_repository(wikipedia_client: WikipediaClient) -> WikipediaRepository:
    return WikipediaRepository(wikipedia_client)


@pytest.fixture(scope='session')
def programming_languages_using_statistics(
    wikipedia_repository: WikipediaRepository
) -> List[ProgrammingLanguagesStatisticEntity]:
    return wikipedia_repository.get_programming_languages_using_statistics()


def test_programming_languages_using_statistics_popularity_more_than_limit_value(
    get_test_data: int,
    programming_languages_using_statistics: List[ProgrammingLanguagesStatisticEntity],
) -> None:
    for statistics_entity in programming_languages_using_statistics:
        pytest.assume(statistics_entity.popularity > get_test_data, (
            f'{statistics_entity.website}(Frontend:{",".join(statistics_entity.front_end)}|'
            f'Backend:{",".join(statistics_entity.back_end)}) has {statistics_entity.popularity} '
            f'unique visitors per month.(Expected more than {get_test_data})”'
        ))
