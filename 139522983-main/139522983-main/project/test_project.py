import pytest
from project import add_expense, total_expense, filter_expenses

@pytest.fixture
def sample_expenses():
    return [
        {"Amount": 20.0, "Category": "Food"},
        {"Amount": 50.0, "Category": "Travel"},
        {"Amount": 30.0, "Category": "Food"}
    ]

def test_add_expense(sample_expenses):
    add_expense(sample_expenses, 100.0, "Entertainment")
    assert sample_expenses[-1] == {"Amount": 100.0, "Category": "Entertainment"}

def test_total_expense(sample_expenses):
    assert total_expense(sample_expenses) == 100.0

def test_filter_expenses(sample_expenses):
    food_expenses = filter_expenses(sample_expenses, "Food")
    assert food_expenses == [
        {"Amount": 20.0, "Category": "Food"},
        {"Amount": 30.0, "Category": "Food"}
    ]

if __name__ == "__main__":
    pytest.main()
