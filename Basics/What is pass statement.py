"""
The pass statement is known as null 
We can use the pass statement as a placeholder when unsure of the code to provide. Therefore, the pass only needs to be placed 
on that line. The pass might be utilized when we wish no code to be executed. We can simply insert a pass in cases where empty 
code is prohibited, such as in loops, functions, class definitions, and if-else statements.

"""

numbers=[1,2,3]

for number in numbers:
    if(number == 2):
        pass
    else:
        print(number)
        

# -----Empty method --------------
def empty_method():
    pass

#-----Empty constructor-----------
class Person:
    def __init__(self) -> None:
        pass