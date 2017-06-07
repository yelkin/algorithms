def valid_brace_sequence(braces: str):
    stack = []

    for brace in braces:
        if brace in '([{':
            stack.append(brace)
        else:
            if len(stack) == 0:
                return False
            brace2 = stack.pop()
            if (brace2 == '(' and brace == ')') or (brace2=='[' and brace == ']') or (brace2 == '{' and brace == '}'):
                continue
            else:
                return False

    return len(stack) == 0


def main():
    valid=[
        '',
        '()',
        '(())',
        '()()()',
        '([{}])',
    ]
    invalid=[
        '(',
        '([)]',
    ]

    for v in valid:
        assert valid_brace_sequence(v), 'Must be valid: %r' % v
    for i in invalid:
        assert valid_brace_sequence(i) == False, 'Must be invalid: %r' % i

    print("All good")


if __name__ == '__main__':
    main()
