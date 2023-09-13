import pytest
import requests_mock
from requests_mock import Mocker

from task_1_pytest.wikipedia_client import ProgrammingLanguagesStatisticEntity, WikipediaClient, WikipediaRepository


class TestWikipediaRepository:
    @pytest.fixture
    def mock_wikipedia_page(self) -> Mocker:
        with requests_mock.Mocker() as mocker:
            mocker.get(
                'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites',
                text='Your mocked HTML content')
            yield mocker

    @pytest.fixture
    def mocked_response_from_wiki(self) -> str:
        return """
        <table>
            <tr>
                <th>Websites</th>
                <th>Popularity</th>
                <th>Front-end</th>
                <th>Back-end</th>
                <th>Database</th>
                <th>Notes</th>
            </tr>
            <tr>
                <td>Website 1</td>
                <td>1000</td>
                <td>HTML,CSS</td>
                <td>Python,Java</td>
                <td>MySQL,PostgreSQL</td>
                <td>Note 1</td>
            </tr>
            <tr>
                <td>Website 2</td>
                <td>2000</td>
                <td>JavaScript</td>
                <td>Node.js</td>
                <td>MongoDB</td>
                <td>Note 2</td>
            </tr>
        </table>
        """

    def test_get_programming_languages_page_success(self, mock_wikipedia_page: Mocker) -> None:
        wikipedia_client = WikipediaClient()
        page = wikipedia_client.get_programming_languages_page()
        assert 'Your mocked HTML content' in page

    def test_get_programming_languages_using_statistics_success(
        self,
        mock_wikipedia_page: Mocker,
        mocked_response_from_wiki: str,
    ) -> None:
        wikipedia_client = WikipediaClient()
        wikipedia_repository = WikipediaRepository(wikipedia_client)

        mock_wikipedia_page.get(
            'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites',
            text=mocked_response_from_wiki,
        )
        result = wikipedia_repository.get_programming_languages_using_statistics()
        assert len(result) == 2
        assert result[0] == ProgrammingLanguagesStatisticEntity(
            website='Website 1',
            popularity=1000,
            front_end=['HTML', 'CSS'],
            back_end=['Python', 'Java'],
            databases=['MySQL', 'PostgreSQL'],
            notes='Note 1'
        )
        assert result[1] == ProgrammingLanguagesStatisticEntity(
            website='Website 2',
            popularity=2000,
            front_end=['JavaScript'],
            back_end=['Node.js'],
            databases=['MongoDB'],
            notes='Note 2'
        )

    def test_get_array_success(self) -> None:
        wikipedia_repository = WikipediaRepository(None)
        assert wikipedia_repository._WikipediaRepository__get_array('a,b,c') == ['a', 'b', 'c']
        assert wikipedia_repository._WikipediaRepository__get_array('') == ['']

    def test_get_numbers_success(self) -> None:
        wikipedia_repository = WikipediaRepository(None)
        assert wikipedia_repository._WikipediaRepository__get_numbers('12345') == 12345
        assert wikipedia_repository._WikipediaRepository__get_numbers('abc123') == 123
        assert not wikipedia_repository._WikipediaRepository__get_numbers('abc')

    def test_remove_references_success(self) -> None:
        wikipedia_repository = WikipediaRepository(None)
        assert wikipedia_repository._WikipediaRepository__remove_references('Some text [1] [2]') == 'Some text  '
        assert wikipedia_repository._WikipediaRepository__remove_references('Some text') == 'Some text'
