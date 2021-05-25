def multi_bracket_validation(input:str)->bool:
    """
    takes a string as its only argument, and return a boolean representing whether or not the brackets in the string are balanced.
    There are 3 types of brackets:

    Round Brackets : ()
    Square Brackets : []
    Curly Brackets : {}
    """
    round_counter = 0
    square_counter = 0
    curly_counter = 0

    for bracket in input:
        if bracket == '(':
            round_counter =+ 1
        elif bracket == '[':
            square_counter += 1
        elif bracket == '{':
            curly_counter += 1

        elif bracket == ')':
            round_counter -= 1
        elif bracket == ']':
            square_counter -= 1
        elif bracket == '}':
            curly_counter -= 1

    if round_counter != 0 or square_counter != 0 or curly_counter != 0:
        return False
    return True


tl = ['{}' ,'{}(){}', '[[()]]', '(({{[))]}}', '()[[Extra Characters]]', '(){}[[]]', '{}{Code}[Fellows](())']
fl =['[({}]', '(](', '{(})']
for st in fl:
    print(multi_bracket_validation(st))

