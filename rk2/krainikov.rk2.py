import lab_python_fp.unique as unique
import lab_python_fp.field as field

def test_unique():
    assert unique.Unique([1, 2, 3, 1, 2, 3]).items == [1, 2, 3]
    assert unique.Unique(["a", "A", "B", "b"], ignore_case=True).items == ["a", "B"]

def test_field():
    workers = [
        {'name': 'Иван', 'surname': 'Иванов', 'age': 25, 'position': 'водитель'},
        {'name': 'Петр', 'surname': 'Петров', 'age': 35, 'position': 'инженер'},
        {'name': 'Алексей', 'surname': 'Алексеев', 'age': 18, 'position': 'стажер'},
    ]
    assert field.field(workers, 'age') == [25, 35, 18]
    assert field.field(workers, 'name') == ['Иван', 'Петр', 'Алексей']
    assert field.field(workers, 'name', 'position') == [{'name': 'Иван', 'position': 'водитель'}, {'name': 'Петр', 'position': 'инженер'}, {'name': 'Алексей', 'position': 'стажер'}]
