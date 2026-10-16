from pyscript import document, display

def Submit(e):

    Grade7 = {"Raven Denum", "Sabine Agacita"}

    Grade8 = {"Frances Sevilla", "Kirsten Caagbay"}

    Grade9 = {"Rodolfo Lao", "Lance Catu"}

    Grade10 = {"Maria Coronel"} # listing members

    GradesAll = Grade7 | Grade8 | Grade9 | Grade10 # putting them together

    NewName = document.getElementById("firstname").value.capitalize() + " " + document.getElementById("lastname").value.capitalize() # getting the input value

    Final = GradesAll | {NewName} # all together

    
    display(Final, target="output1")

    display(len(Final), target="output2")






























#colors = {'green', 'yellow', 'pink', 'blue', 'PINK'}

#colors.add('red')

# set1 = {1, 1.15, "number"}

#set1 = {'apple', 'banana', 'cherry'}

#set2 = {'pineapple', 'banana', 'melon', 'watermelon', 'cherry'}

# A = {'burger', 'fries'}

# B = {'burger', 'fries', 'coke', 'pie'}



#display(, target="output1")

#display(set2 - set1, target="output1")
