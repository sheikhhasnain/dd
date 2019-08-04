def valueseparation(prompt):
    prompt = prompt.strip()
    operator = prompt[0]
    value = int (prompt[1:])
    
    return operator, value