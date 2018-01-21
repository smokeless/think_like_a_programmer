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
    for i in range(2, 10, 2):
        print(' ' * spacer, '#' * i)
        spacer -= 1

diamond()

