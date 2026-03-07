import operator
operations = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': operator.truediv,
    'mod': operator.mod,
    'pow': operator.pow
}
varValues = {}
stacksVarValues = {}


# This is for printing the output of the program. It checks if the first token is 'print' and then prints the second token. If there are more than 2 tokens, it joins them together and prints the resulting string.
def printEval(tokens):
    if tokens[0] == 'print':
        if len(tokens) == 2 and tokens[1] not in varValues and tokens[1] not in stacksVarValues:
            tokens[1] = tokens[1].strip().strip('""')  # Remove any leading/trailing whitespace
            print(tokens[1])
        elif tokens[1] in varValues :
            print(varValues[tokens[1]])
            return
        elif tokens[1] in stacksVarValues:
            print(stacksVarValues[tokens[1]])
            return
        else:
            sentance = " ".join(tokens) # joins the remaining tokens into a single string 
            clean = sentance.replace('"', '').replace('(', '').replace(')', '') # removes any parentheses and quotes from the string
            print(clean)



def varEval(tokens):
    if '=' not in tokens:
        return
    eq_index = tokens.index('=')
    var = tokens[0]
    if eq_index == len(tokens) - 1:
        print(f"Invalid statement {var} = ??")
        quit()
    expr = tokens[eq_index + 1:]

    if expr[-1] in operations.keys():
            varValues[var] = mathOpsEval(expr[:])
    else:
        try:
            varValues[var] = float(expr[0])
        except ValueError:
            varValues[var] = expr[0].strip('"')  # Remove quotes if it's a string




def mathOpsEval(tokens):
    op = tokens[-1]
    nums = []
    try:
        for token in tokens[0:-1]:
            if token in varValues:
                nums.append(float(varValues[token]))
            else:
                nums.append(float(token))
    except ValueError:
        print(f"Invalid number: {token}")
        return
    if op in operations:
        result = nums[0]
        for num in nums[1:]:
            result = operations[op](result, num)
        if result.is_integer():
            return int(result)
        return(result)
    else:
        print(f"Unknown operation: {op}") 


def stacksVarEval(tokens):
    var = tokens[0]
    old_value = tokens[1].replace("'", "").replace("[", "").replace("]", "")
    new_value = list(old_value.split(','))
    stacksVarValues[var] = new_value


def stackAppend(var, value):
    if var in stacksVarValues:
        stacksVarValues[var].append(value)
    else:
        stacksVarValues[var] = str(value)

def stackPop(var, value = None):
    if var in stacksVarValues and stacksVarValues[var]:
        stacksVarValues[var].pop()

def stackDel(var, index):
    if var in stacksVarValues and 0 <= index < len(stacksVarValues[var]):
        del stacksVarValues[var][index]


stackOperations = {
    'append': stackAppend,
    'pop': stackPop,
    'del': stackDel
}

def exec():
    if tokens[0] == 'print':
        printEval(tokens)
    elif tokens[0] == 'math':
        tokensCpy = tokens[1:]
        mathOpsEval(tokensCpy)
    elif tokens[0] == 'var':
        tokensCpy = tokens[1:]
        varEval(tokensCpy)
    elif tokens[0] == 'stack':
        if tokens[1] in stackOperations:
            stackOperations[tokens[1]](tokens[2], int(tokens[3]) if len(tokens) > 3 else None)
        else:       
            stacksVarEval(tokens[1:])

with open("program.my", 'r') as file:
    for line in file:
        tokens = [token.strip() for token in line.strip('\n').split() if token.strip() != '']
        if tokens:  # Check if the line is not empty
            exec()