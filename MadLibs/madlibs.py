def playMadlib():
    print("Welcome to madlibs!")

    with open('prompt.txt') as f:
        prompt = f.read()
        
    prompt = prompt.split("_")    
    finalString = []
    for i, v in enumerate(prompt):
        if i % 2 == 1:
            finalString.append(input(f"Give me a {v}: "))
        else:
            finalString.append(v)
    print("".join(finalString))
    
playMadlib()