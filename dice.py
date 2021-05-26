#Click "Run" to roll the dice...

typeofdice = input("How many sides do you want? (Enter 1, 4, 6, 10, or 12) ")
#six sided dice
import random
number = ['1','2','3','4','5','6']

r_n = random.choice(number)

if typeofdice == "6",
    print ''
    print ''
    print '--Dice Roll--'
    print ''
    print '*6 sided dice*'

    if r_n == '1':
        print '_______'
        print '|     |'
        print '|  O  |'
        print '|     |'
        print '‾‾‾‾‾‾‾'
  
    if r_n == '2':
        print '_______'
        print '|O    |'
        print '|     |'
        print '|    O|'
        print '‾‾‾‾‾‾‾'
  
    if r_n == '3':
        print '_______'
        print '|O    |'
        print '|  O  |'
        print '|    O|'
        print '‾‾‾‾‾‾‾'
  
    if r_n == '4':
        print '_______'
        print '|O   O|'
        print '|     |'
        print '|O   O|'
        print '‾‾‾‾‾‾‾'
  
    if r_n == '5':
        print '_______'
        print '|O   O|'
        print '|  O  |'
        print '|O   O|'
        print '‾‾‾‾‾‾‾'
  
    if r_n == '6':
        print '_______'
        print '|O   O|'
        print '|O   O|'
        print '|O   O|'
        print '‾‾‾‾‾‾‾'

    print 'The dice rolled:', str(r_n)


#four sided dice
import random
dice4 = ['1','2','3','4']

triangle = random.choice(dice4)

print ''
print'*4 sided dice*'

if triangle == '1':
  print "  / \  "
  print " / O \ "
  print "/     \ "
  print "‾‾‾‾‾‾‾"
 
if triangle == '2':
  print "  / \  "
  print " /O  \ "
  print "/   O \ "
  print "‾‾‾‾‾‾‾"
  
if triangle == '3':
  print "  / \  "
  print " / O \ "
  print "/ O O \ "
  print "‾‾‾‾‾‾‾"
  
if triangle == '4':
  print "  / \  "
  print " /O O\ "
  print "/ O O \ "
  print "‾‾‾‾‾‾‾"

print 'the dice rolled', str(triangle)
