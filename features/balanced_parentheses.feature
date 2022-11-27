Feature: Balanced Parentheses

Scenario Outline: A string is Balanced if the left and right parentheses match correctly
Given the expression "<expression>" 
When string is checked for balanced parentheses 
Then the result is "<balanced>"

Examples:
| expression | balanced |
| ''         | True     |
| '((()))'   | True     |
| '[()]{}'   | True     |
| '({[)]'    | False    |
