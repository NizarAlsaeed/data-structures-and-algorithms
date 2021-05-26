def multi_bracket_validation(input:str)->bool:
    """
    takes a string as its only argument, and return a boolean representing whether or not the brackets in the string are balanced.
    There are 3 types of brackets:

    Round Brackets : ()
    Square Brackets : []
    Curly Brackets : {}
    """
    openers = ['(', '[', '{']
    closers = [')', ']', '}']
    holder = []

    #cleaning non brkts chars:
    for char in input:
        if not ((char in openers) or (char in closers)):
            input = input.replace(char, '')

    print(input)
    # if the brkts are not even (must be even to be balanced)
    if len(input) %2 != 0:
        return False

    for bracket in input:

        if (bracket in closers):
            if len(holder)==0:
                return False

            if holder:
                if holder[-1] in openers:
                    # means that if the latest opening brkt added to holder is of the same type of the latest closing brkt?
                    if openers.index(holder[-1]) == closers.index(bracket):
                        holder.append(bracket)
                    else:
                        return False
            else:
                holder.append(bracket)
        else:
            holder.append(bracket)

    return True

if __name__ == '__main__':

    tl = ['{}' ,'{}(){}', '[[()]]','()[[Extra Characters]]', '(){}[[]]', '{}{Code}[Fellows](())']
    fl =['[({}]', '(](', '{(})']
    for st in fl:
        print(multi_bracket_validation(st))
