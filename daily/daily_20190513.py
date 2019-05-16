test_cases = [
    '()',
    '(())',
    '()()',
    '([])',
    '([])',
    '([)]',
    '{{}()[()]}',
    '{[]{()}{{{{{{}',
]

#b_open = ['(', '[', '{']
#b_close = [')', ']', '}']

brackets = dict()
brackets['('] = ')'
brackets['['] = ']'
brackets['{'] = '}'

def is_balanced(s: str) -> bool:
    stack = list()
    for c in s:
        if c in brackets.keys():
            stack.append(c)
        elif c in brackets.values():
            d = stack.pop()
            if brackets[d] != c:
                return False
    if len(stack):
        return False
    return True

for tst in test_cases:
    print("Test case:", tst, "Result:", is_balanced(tst))