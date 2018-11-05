#Andrew Vu
#Prof. Wang
#CPSC 485-01
#Due: Nov. 15, 2018

#This program was built using Python 3.7.0. with they PyCharm IDE built by JetBrains
#Please note this is different than Python 2.x
#Program can be compiled and ran using PyCharm with 3.7.0 shell integrated.
#In PyCharm you can right click in anywhere of the file(where you can type in code), and go to "Run" option.
#The option "Run" is also located on the top navigation bar, where you can have access to run the program
#You can also press "ctrl + shift + F10" on a windows computer to run


print("Please enter two words (up to 30 characters).")

print("Please enter the 1st word: ", end ="")
word1 = input()

print("Please enter the 2nd word: ", end ="")
word2 = input()

#initialized my variables
editArray=[]
maxlen1 = len(word1)
maxlen2 = len(word2)
alignWord1 = word1
alignWord2 = word2

def initializeArray(word1, word2):
    for i in range (0, (len(word1) + 1)):
        editArray.append([])
        for j in range (0, (len(word2) + 1)):
            editArray[i].append(j)
            if j == 0:
                editArray[i][j] = i
            elif i == 0:
                editArray[i][j] = j
            else:
                editArray[i][j] = 0


def doEdit(word1,word2):
    for i in range (1, (len(word1)+1)):
        for j in range(1, (len(word2)+1)):
            edit(i,j)

# changes the values of my matrix between two strings
def edit(i, j):
    x=i-1
    y=j-1
    if word1[x] == word2[y]:
        diagonal = editArray[x][y]
    else:
        diagonal = editArray[x][y] + 1
    top = editArray[x][j] + 1
    left = editArray[i][y] + 1
    editArray[i][j] = min(diagonal,top,left)



####For styling output
def displayArray(word1, word2):
    print("\nThe matrix:", end="\n\n")
    for i in range(0, (len(word2) + 1)):
        print("\t " + str(i), end="")
    print("\n", end="")
    border(word2)
    for i in range (0, len(word1)+1):
        print(str(i) + "|", end = "")
        for j in range (0, len(word2)+1):
            print("\t " +str(editArray[i][j])+":",end ="")
        print("")
        border(word1)


####For styling output
def border(word):
    print("  ", end = "")
    for i in range (0,len(word1) + 1):
        print("-------", end="")
    print("")

#recursively obtain the alignment between two strings working from the last element of the 2D Array to [0,0]
def align(maxlen1,maxlen2,alignWord1 ,alignWord2):
    #created diagonal left and up variable
    #used to compare values at my specific point in the matrix
    #ex. if i'm at [7][7] i look at [6][7], [6][6], [7][6], then I choose my path
    diagonal = editArray[maxlen1-1][maxlen2 -1]
    left = editArray[maxlen1][maxlen2-1]
    up = editArray[maxlen1 - 1][maxlen2]

    #base case of recursion prints out the alignment
    if maxlen1 == 0 and maxlen2 == 0:
        print("Alignment is:")
        print(alignWord1)
        print(alignWord2)
        return
    #if my y = 0 then move up one spot above of the current position in the matrix
    elif maxlen1 > 0 and maxlen2 == 0:
        alignWord2 =  '_' + alignWord2
        align(maxlen1 - 1, maxlen2, alignWord1, alignWord2)
    # if my x = 0 then move up one spot to the left of the current position in the matrix
    elif maxlen2 > 0 and maxlen1 == 0:
        alignWord1 =  '_' + alignWord1
        align(maxlen1, maxlen2 - 1, alignWord1, alignWord2)
    #if the value is less in the diagonal, then move diagonally
    elif diagonal < editArray[maxlen1][maxlen2]:
        align(maxlen1-1, maxlen2-1,alignWord1,alignWord2)
    #if up is the min value move up one spot above the current position in the matrix
    #align the word with an '_'
    elif up < diagonal and up < left:
        alignWord2 = alignWord2[:maxlen1] + '_' + alignWord2[maxlen1:]
        align(maxlen1-1, maxlen2, alignWord1, alignWord2)
    # if left is the min value move up one spot to the left the current position in the matrix
    # align the word with an '_'
    elif left < diagonal and left < up:
        alignWord1 = alignWord1[:maxlen2]+ '_' + alignWord1[maxlen2:]
        align(maxlen1, maxlen2-1, alignWord1, alignWord2)
    #if everything is equal go diagonal
    else:
        align(maxlen1 - 1, maxlen2 - 1, alignWord1, alignWord2)



def main(word1,word2):
    #initialize the array
    initializeArray(word1, word2)
    #changes the values in the array
    doEdit(word1, word2)
    #displays the array
    displayArray(word1, word2)
    print("\nThe edit distance is: " + str(editArray[len(word1)][len(word2)]))
    #finds the alignment
    align(maxlen1, maxlen2, alignWord1, alignWord2)


if maxlen1 == 0 or maxlen2 == 0:
    print("Please REDO the program and enter two PROPER strings for comparison")
else:
    main(word1,word2)







