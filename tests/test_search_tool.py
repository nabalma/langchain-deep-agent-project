# from pathlib import Path
# from pprint import pprint
# import sys

# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# sys.path.insert(0, str(PROJECT_ROOT))

# from tools.search_tool import internet_search


# def main():
#     results = internet_search(
#         query="What is C3G at McGill University ?",
#         max_results=2,
#     )

#     print("\nTYPE:")
#     print(type(results))

#     print("\nRESULTS:")
#     pprint(results)

#     print("\nCHECK:")
#     print("Number of results:", len(results))

#     if results:
#         first_result = results[0]
#         print("First result keys:", first_result.keys())


# if __name__ == "__main__":
#     main()


from pathlib import Path
from pprint import pprint
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from tools.search_tool import internet_search


MAX_RESULTS = 1

@pytest.fixture(scope="module")
def search_results():
    results = internet_search(
        query="What is LangGraph?",
        max_results =MAX_RESULTS,
    )

    return results


@pytest.fixture(scope="module")
def first_result(search_results):
    assert isinstance(search_results, list)
    assert len(search_results) > 0
    return search_results[0]


def test_should_return_a_list_of_search_results(search_results):
    assert isinstance(search_results, list)


def test_should_return_title_key(first_result):
    assert "title" in first_result


def test_should_return_url_key(first_result):
    assert "url" in first_result


def test_should_return_content_key(first_result):
    assert "content" in first_result


def test_should_not_return_more_than_max_results(search_results):
    assert len(search_results) <= MAX_RESULTS