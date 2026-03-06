import operator

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
            print(stacksVarValues)
            return
        else:
            sentance = " ".join(tokens) # joins the remaining tokens into a single string 
            clean = sentance.replace('"', '').replace('(', '').replace(')', '') # removes any parentheses and quotes from the string
            print(clean)


varValues = {}
def varEval(tokens):
    var = tokens[0]
    if isinstance(tokens[-1], str):
        varValues[var] = tokens[-1].strip('"').strip('.')
    else:
        value = float(tokens[-1]) 
        varValues[var] = value


operations = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': operator.truediv,
    'mod': operator.mod,
    'pow': operator.pow
}
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
            print(int(result))
            return
        print(result)
    else:
        print(f"Unknown operation: {op}") 


stacksVarValues = {}
def stacksVarEval(tokens):
    var = tokens[0]
    old_value = tokens[1].replace("'", "").replace("[", "").replace("]", "")
    new_value = list(old_value.split(','))
    stacksVarValues[var] = new_value


def stackAppend(var, value):
    if var in stacksVarValues:
        stacksVarValues[var] += str(value)
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
        tokens.pop(0)
        mathOpsEval(tokens)
    elif tokens[0] == 'var':
        tokens.pop(0)
        varEval(tokens)
    elif tokens[0] == 'stack':
        if tokens[1] in stackOperations:
            stackOperations[tokens[1]](tokens[2], int(tokens[3]) if len(tokens) > 3 else None)
        else:       
            stacksVarEval(tokens[1:])

with open("program.my", 'r') as file:
    for line in file:
        tokens = line.strip('\n').split()
        if tokens:  # Check if the line is not empty
            exec()