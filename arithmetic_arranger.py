# This code is related to the Arithmetic Arranger Chalenger. The description of the requirements are on the link bellow
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def arithmetic_arranger(problems, bool=None):
     
    arranged_problems = ""   
    draft = []
    
    # setting rules:
    if len(problems) < 1 or len(problems) > 5:
        return "Error: Too many problems."   
        
    for index, value in enumerate(problems):
        
        # splitting the operators
        parts = value.split(" ")
        
        if parts[1] not in '+-':
            return "Error: Operator must be '+' or '-'."  
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # getting the spacing regarding the longest operand
        
        max_len = max(len(parts[0]), len(parts[2]))

        # drafiting an output
        ln1 = f"{parts[0]:>{max_len+2}}"
        ln2 = f"{parts[1]}{' '*(max_len+1-len(parts[2]))}{parts[2]}"
        ln3 = '-'*(max_len+2)
        
        try:
            draft[0] += (' ' * 4) + ln1
            
        except IndexError:
            draft.append(ln1)
        try:
            draft[1] += (' ' * 4) + ln2
        except IndexError:
            draft.append(ln2)
        try:
            draft[2] += (' ' * 4) + ln3
        except IndexError:
            draft.append(ln3) 
        
        # getting the answer
        if bool == True:
            if '+' in parts[1]:
                tot = int(parts[0]) + int(parts[2])

            if '-' in parts[1]:
                tot = int(parts[0]) - int(parts[2])   

            ln4 = f"{tot:>{max_len+2}}"
            
            try:
                draft[3] += (' ' * 4) + ln4
            except IndexError:
                draft.append(ln4)
    
    # Final formated output
    try:
        arranged_problems =  f"{draft[0]}\n{draft[1]}\n{draft[2]}\n{draft[3]}"

    except:
        arranged_problems =  f"{draft[0]}\n{draft[1]}\n{draft[2]}"
            
   
    return arranged_problems
        
