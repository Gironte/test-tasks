from dataclasses import dataclass
from enum import Enum
import re
from typing import List, Optional

from bs4 import BeautifulSoup
import requests


class ProgrammingLanguagesTableHeadersNamesParts(Enum):
    WEBSITES = 'Websites'
    POPULARITY = 'Popularity'
    FRONTEND = 'Front-end'
    BACKEND = 'Back-end'
    DATABASE = 'Database'
    NOTES = 'Notes'


@dataclass(frozen=True)
class ProgrammingLanguagesStatisticEntity:
    website: str
    popularity: int
    front_end: list[str]
    back_end: list[str]
    databases: list[str]
    notes: str


class WikipediaClient:
    __WIKIPEDIA_BASE_URL = 'https://en.wikipedia.org/wiki'

    def get_programming_languages_page(self) -> str:
        response = requests.get(f'{self.__WIKIPEDIA_BASE_URL}/Programming_languages_used_in_most_popular_websites')
        return response.text


class WikipediaRepository:
    def __init__(self, wiki_client: WikipediaClient) -> None:
        self.__wiki_client = wiki_client

    def get_programming_languages_using_statistics(self) -> List[ProgrammingLanguagesStatisticEntity]:
        html = self.__wiki_client.get_programming_languages_page()
        table = BeautifulSoup(html, 'html.parser').find('table')
        headers_texts = [header.getText() for header in table.find_all('tr')[0].find_all('th')]
        headers_indexes = {
            enum.value: column_number for column_number, enum in enumerate(ProgrammingLanguagesTableHeadersNamesParts)
            if
            any(enum.value in header for header in headers_texts)
        }
        result = []
        for row in table.find_all('tr')[1:]:
            cells_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            entity = ProgrammingLanguagesStatisticEntity(
                website=self.__remove_references(
                    cells_data[
                        headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.WEBSITES.value, None)]
                ),
                popularity=self.__get_numbers(
                    cells_data[
                        headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.POPULARITY.value, None)]
                ),
                front_end=self.__get_array(
                    cells_data[
                        headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.FRONTEND.value, None)]
                ),
                back_end=self.__get_array(
                    cells_data[
                        headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.BACKEND.value, None)]
                ),
                databases=self.__get_array(
                    cells_data[
                        headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.DATABASE.value, None)]
                ),
                notes=self.__remove_references(
                    cells_data[headers_indexes.get(ProgrammingLanguagesTableHeadersNamesParts.NOTES.value, None)]
                )
            )
            result.append(entity)
        return result

    def __get_array(self, inner_text: str) -> List[str]:
        text = self.__remove_references(inner_text)
        return text.split(',')

    def __get_numbers(self, inner_text: str) -> Optional[int]:
        text = self.__remove_references(inner_text)
        digits = ''.join(re.findall(r'\d+', text))
        if digits.isdigit():
            return int(digits)
        else:
            return None

    def __remove_references(self, inner_text: str) -> str:
        return re.sub(r"\[\d+]", '', inner_text)
