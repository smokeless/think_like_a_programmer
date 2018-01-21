'''Chapter 2 challenges'''

'''
Using the same rule as the shapes programs from earlier in the chapter 
(only two output statements—one that outputs the hash mark and one that 
outputs an end-of-line), write a program that produces the following shape:
             ########
              ######
               ####
                ##
'''

def upside_down_triangle():
    '''Write a program that uses only two output
    statements, cout << "#" and cout << "\n",
    to produce a line of five hash symbols:
    #####'''
    i = 8
    spaces = 0
    while i > 1:
        print((' ' * spaces) + '#' * i)
        i -= 2
        spaces += 1

def diamond():
    '''2-2. Or how about:
           ##
          ####
         ######
        ########
        ########
         ######
          ####
           ##'''
    spacer = 4
    i = 8
    hashMarks = 2
    flipMarks = False
    while i > 0:
        i -= 1
        if hashMarks == 10 or flipMarks == True:
            hashMarks -= 4
            flipMarks = True
            spacer += 2
        print(' ' * abs(spacer), '#' * abs(hashMarks))
        spacer -= 1
        hashMarks += 2

diamond()

