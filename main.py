from pyscript import document, display

def Submit(e)

    Grade7 = {"Raven", "Sabine"}

    Grade8 = {"Frances", "Kirsten"}

    Grade9 = {"Rodolfo", "Lance"}

    Grade10 = {"Maria"}

    GradesAll = Grade7 | Grade8 | Grade9 | Grade10

    NewName = document.getElementById("firstname").value + " " + document.getElementById("lastname").value

    GradesAll.add('')

    display(NewName, target="output1")






























#colors = {'green', 'yellow', 'pink', 'blue', 'PINK'}

#colors.add('red')

# set1 = {1, 1.15, "number"}

#set1 = {'apple', 'banana', 'cherry'}

#set2 = {'pineapple', 'banana', 'melon', 'watermelon', 'cherry'}

# A = {'burger', 'fries'}

# B = {'burger', 'fries', 'coke', 'pie'}



#display(, target="output1")

#display(set2 - set1, target="output1")
