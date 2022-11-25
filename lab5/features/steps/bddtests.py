from behave import given, when, then, step
import lab_python_fp.unique as unique
import lab_python_fp.field as field

@given('a list of numbers')
def step_impl(context):
    context.list_of_numbers = [1, 2, 3, 1, 2, 3]

@when('we call Unique')
def step_impl(context):
    context.unique = unique.Unique(context.list_of_numbers)

@then('we get a list of unique numbers')
def step_impl(context):
    assert context.unique.items == [1, 2, 3]

@given('a list of strings')
def step_impl(context):
    context.list_of_strings = ["a", "A", "B", "b"]

@when('we call Unique with ignore_case=True')
def step_impl(context):
    context.unique = unique.Unique(context.list_of_strings, ignore_case=True)

@then('we get a list of unique strings')
def step_impl(context):
    assert context.unique.items == ["a", "B"]

@given('a list of dictionaries')
def step_impl(context):
    context.workers = [
        {'name': 'Иван', 'surname': 'Иванов', 'age': 25, 'position': 'водитель'},
        {'name': 'Петр', 'surname': 'Петров', 'age': 35, 'position': 'инженер'},
        {'name': 'Алексей', 'surname': 'Алексеев', 'age': 18, 'position': 'стажер'},
    ]

@when('we call field with "age"')
def step_impl(context):
    context.result = field.field(context.workers, 'age')

@then('we get a list of ages')
def step_impl(context):
    assert context.result == [25, 35, 18]