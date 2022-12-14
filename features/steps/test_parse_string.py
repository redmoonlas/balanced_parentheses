from behave import *
from parse_string import check_parentheses


@given('the expression "{expression}"')
def step_impl(context, expression):
    context.expression = expression


@when(u'string is checked for balanced parentheses')
def step_impl(context):
    context.balanced = check_parentheses(context.expression)


@then(u'the result is "{balanced}"')
def step_impl(context, balanced):
    balanced = True if balanced == 'True' else False
    assert context.balanced == balanced
