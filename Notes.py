ELements of python

- Vocabulary/words: variables and reserved words
- sentence structure: valid syntax patterns
- story structure: constructing a program for a purpoose.




Sequential() repeated(loop) confitional(if)

Chapter 2 : Variables. expression. statements.

1. constants
fixed value such as numbers, letters, and strings...value does not hcange.
-numeric constants are as you expect
-string sonstants use single quotes('') or double qoutes("")

2. Reserved words
- you cannot use reserved words as varible names/identifiers.

False   class    return   is      finally
None    if       for      lambda  continue
True    def      from     while   nonlocal
and     del      global   not     with
as      elif     try      or      yield
assert  else     import   pass
break   except   in       raise

3. Variables
-a variable is a names place in the memorty where a
programmer can store data and later retrieve the data using variable"name"
- programmers get to choose the name of the Variables
- you can change the contents of a variable in a later statement.

4. python variable name rules
-must start with a letter or underscore_
- must consist of letters, numbers, and underscores.
- case sensitive
        good: spam  eggs    spam23  _speed
        bad: 23spam #sign   var.12
        different: spam Spam  SPAM

5. Mnemonic Variable names
- since we programmers are given a choice in how we choose our variable names.
- people names variables to help remember what we intend to store in them.
("mnemonic"="memory aid")

6. Sentence or Lines
x=2 //assignmenr statement
x=x+2  //assignmenr with expression
print(x)  //print statement.

7. assignment statements
- we assign a value to a variable using the assignment statement(=)
- an assignment statement consists of an experessionon the right-hand side and a
variable to store the result.
 on the = right process first then left of =.

 For example:
          x=0.6 ---> x=3.9 * x * (1-x). --> x=0.93
- the variable x is a memory location used to store a value (0.6)
- the right side is an experession.
- once the expression is evaluatd, the result is placed in (assigned to) the variable
  on the lieft side which in this case is x.
- a vatiable is a memory location used to store a value. The value stored in a variable
  can be updated by replaceing the old value(0.6 with a new value(0.93)

 8. Numeric Expressions.

    operator: addition+ subtraction- multiplication* division/ power** remainder%

example: >>>jj=23
         >>>kk=jj % 5
         >>>print(kk)
         3

9. Order of Evaluation
 - operator precendence: which operators to do first
 - operator precedence rules: parenthesis, power, multiplication, addition, left to right.

10. Type
- can not add 1 to a string.
- we can ask python what type something is by using type() function.
- several types of numbers: integers, floating point numbers,
- type conversions: when an interger and floating point in an expression,
  the integer is implicitly converted to a float. And you can control this with
  the built-in functions int() and float().
  exapmle:>>>print(float(99) + 100)
          199.0
          >>>i = 42
          >>>type(i)
          <class'int'>
          >>>f = float(i)
          >>>print(f)
          42.0

11. integer division
- interger division produces a floating point result.

12. string conversions(only valued for strings that made of digits)
-use int() and float() to convert between strings and integers.
    example:>>> a = '123'
            >>> type(a)
            <class'str'>
            >>>print(a + 1)
            Error
            >>> b = int(a)
            >>> type(b)
            <class'int'>
            >>> print(b + 1)
            124

13. User Input
- we can instruct python to pause and read data from the user using the input() function.
- the input() function returns a strings.

14. converting user Input
- if we want to read a number from the user, we must convert it from a string to a number using
  a typr conversion function.

15. comments in python
- start with #


CHAPTER 3 Conditional Execution

1. condition seps
    porgram:
            x = 5
            if x < 10:
                print('smaller')
            if x > 20:
                print('bigger')

            print('Finis')

2. comparison operators
- Boolean expressions ask a question and produce a Yes or No result which we use to control program flow.
- Boolean expressions using comparison operators evaluate to Ture/False or Yes/No.
- Comparison operatiors look at variables but do not change the variables.

python:
        <                   Less than
        <=                  Less than or equal to
        ==                  Equal to
        >=                  Greater tha or equal to
        >                   Greater than
        !=                  Not equal

3. Indentation
- Increase indent indent after an if statement or for statement (after : )
- Maintain indent to indicate the scope of the block (which lines are affected by the if/for)
- Reduce indent back to the level of the if statement or for statement to indicate the end of the block.

4. Warning: Tuen off Tabs.
- pyhton cares a "lot" about how far a line is indented. if you mix tabs and spaces,
you may get "indentation errors" even if everything look fine.
- example:
            x = 5
            if x > 2 :
                print('binnger than 2')
                print('still bigger')
            print('done with 2')

            for i in range(5) :
                print(i)
                if i > 2 :
                    print('biger than 2')
                print('done with i', i)
            print('All done')

5. Nested Decisions
- example:
            x = 42
            if x > 1 :
                print('more than one')
                if x < 100 :
                    print('less than 100')
            print('all done')

6. Two way Decisions
- choose one or the other path but not both.
- exapmle:
            x = 4
            if x > 2 :
                print('bigger')
            else :
                print('smaller')

            print('all done')

7. multi- way branch
- example:
            if X < 2 :
                print('small')
            elif x < 10 :
                print('medium')
            else :
                print('large')
            print('all done')
8. the try / except structure
-  compensate for errors.
- example:
            rawstr = input('enter a number: ')
            try:
                ival = int('rawstr')
            except:
                ival = -1

            if ival > 0 :
                print('nice work')
            else :
                print('not a number')

CHAPTER 4 : functions

1. python functions
- build-in functions : print() input() float() int()
- functions that we define ourselves and then use.

2. function definition
- function is some reusable code that takes arguments as input,
does osme somputation, and then returns a result or results
- define a function use  def
- call/invoke the function by using the function name, parentheses and srguments in an expression.

3. type comversions
- integer and floating point in an epression, the integer is imp;ocotly converted to a float.
- but you can control this byusing int() float()

4. string conversions
- can convert str to int , only fr numeric str.

5. arguments
- an argument is a value we pass into the function as its input when we call the function.
- we use arguments so we can direct the function to do different kinds of work when
we call it at different times.
- put the arguments in parentheses after the name of the function.

6. parameters
- place holder
- a parameter is a variable which we use in the function deinition. It is a "handle"
that allows the code in the function to access the arguments for a particular function
invocation.

>>>def greed(lang):
       if lang == 'es':
           print('hola')
       elif lang == 'fr':
           print('bonjour')
       else:
           print('hello')
>>>greed('en')
hello
>>>greed('fr')
bonjour

7. return value
- get things out of def function
- the first return run then it will stop there.
- a fruitful unction is one that produce a result (or return value)
- the return statement ends the function execution and 'send back' the result of the function.
example:
            >>>def greed(lang):
                   if lang == 'es':
                       return 'hola'
                   elif lang == 'fr':
                       return 'bonjour'
                   else:
                       return 'hello'
            >>>print(greed('fr'), 'John')
            bonjour John

8. multipul parameters/arguments
- can define more than one parameters in the function definition.
- simply add more arguments when we call the function
- match the number adn order of argumens and parameters.

example:   def addtwo(a, b) :
               added = a + b
               return added

           x = addtwo(3, 5)
           print(x)

           8

9. void (non-fruitful) function
- the function does not return value

************************************CHAPter 5 Lteration

1.repeated steps
- loop(repeated steps) have iteration vriables that change
each time through a loop. Often these iteration vriables go through a sequence
of numbers.

2. an infinite loop
- constant true...

3. break out of a loop
- break statement ends the current loop and jump to the
atatement immediately following the loop.
- can happen anywhee n the body of the loop
example: while ture:
            line = input('> ')
            if line == 'done' :
                break
            print(line)
         print('done!')

4. finishing an iteration with continue
- continue statement ends the current iteration and jumps to the
top of he loop and starts the next iteration.

5. indefinite loops
- keep going until a logical condition become false.

for most of loop we use definite loop.

6. definite loops
- use for key word.
- going to loop set of things( strings, files .....)
exapmle: for i in [1, 2, 3, 4, 5] :
             print(1)
         print('blastoff')
i here is iteration variable, those numbers are elements sequence
 - the iteration variable "iterates" through the sequence(ordered set)
 - the block(body) of code is executed once for each value in the sequence
 - the iteration variable moves through all of the values in the sequence.



 - find the largest value:
 largest_so_far = -1
 print('before', largest_so-far)                            before-1
 for the_num in [9, 42, 12, 3, 74, 15] :                    9 9
     if the_num > largest_so_far :                          42 42
         largest_so_far = the_num                           42 12
     print(largest_so_far, te_num)                          ...
 print('after', largest_so_far)                             after74

 7. counting in a loop
zork = 0
print('before', zork)
for thing in [9, 42, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('after', zork)

8. summing in a loop
 zork = 0
 print('before', zork)
 for thing in [9, 42, 12, 3, 74, 15] :
     zork = zork + thing
     print(zork, thing)
 print('after', zork)

9. finding the average in a loop.

count = 0
sum = 0
print('before', count, sum)
for value in [9, 42, 12, 3, 74, 15] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum/count)

10. filtering in a loop

print('before')
for value in [9, 42, 12, 3, 74, 15] :
    if value > 20 :
        print('large numer', value)
print('after')

11. searvhing using a boolean variable(true/False)

found = False
print('before', found)
for value in [9, 42, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('after', found)

checking for 3, if we have 3 it remains true for the reat of loop.
how about we put a break to make this loop more effciency ???????????

12. how to find a smallest value
- None type has one value : None(constant value) often use to indicate emptyness.
- is is more stronger than ==
- the first time thorugh the loop smallest is none. so we take the first value to be the smallest.

 smallest_so_far = None
 print('before', smallest_so-far)                            before
 for value in [9, 42, 12, 3, 74, 15] :                       9 9
     if smallest is None :
         smallest = value
     elif value < smallest :
         smallest = value
     print(smallest, value)
print('after', smallest)

13. the 'is' and 'is not' operators
- is operator that can be used in logical Expressions.
- implies "is the same as"
- similar, but stronger than ==
- is not also logical
- use it on booleans, none types.

*****************************************************CHAPTER 6 strings

1. string type
- in string + means concatenate.
- raw input numbers must be converted from strings.

2. Index in strings
- can get any single character in a string using index specified in square brackets.
- the index value must be an integer and started at zero.
example :>>>fruit = 'banana'
         >>>letter = fruit[1]
         >>>print(letter)
         a
- can not index beyound the length of string.

3. length of strings
- buid-in function len gives us the length of a string.
example: >>>fruit = 'banana'
         >>>print(len(fruit))
         6

4. looping through strings
- using a while staement and an iteration variable, and the len function fnction,
we can cosntruct a loop to look at each of the letters in a string individually.
example: fruit = 'banana'
         index = 0
         while index < len(fruit) :
             letter = fruit[index]
             print(index, letter)
             index = index + 1

- use for loop is more elegant(more prefer)
- the iteration variable is completely thaken care of by for loop
example: fruit = 'banana'
         for letter in fruit :
             print(letter)

5. look deeper into in
- the iteration variable 'iterates' through the dtring and the block(index) of
code is executed once for each value in the sequence.

6. slicing strings
- the second number is one beyond the end of the slice 'up to but not including'
- if second number is beyound the end of string, its going to stop at the thend of string.
example:
>>> s = 'monty python'
>>> print(s[0:4])
mont
>>>print(s[6:7])
p
>>>print(s[6:20])
python
>>>print(s[:4])
mont

7. string concatenation
-if want to add space in string use +
e.g. c = a + ' ' + 'hello'

8. using in as a logical operator
exapmle:
>>>fruit = 'banana'
>>>'n' in fruit
True
>>>'m' in fruit
False

9. string comparison
- upper < lower case
example:
if word == 'banana'
  print ('all right, banana')
if word < 'banana':
    print('your word,' + word + 'behind banana')

10. string library
example:
>>>greet = 'Hello Bob'
>>>zap = greet.lower()
>>>print(zap)
hello Bob
>>>print(greet)
Hello Bob

11.searching a strings
- find() function
- find() fnds the first occurrence of the substring
- if the substring is not found, find() returns -1
- remember string position starts at zero.
example:
>>>fruit = 'banana'
>>>pos = fruit.find(na)
>>>print(pos)
2

12. make ecerthing upper case or lower case
- ofeten when we are searching for a string using find() we first convert
the string to lower caes so we can search a string regardless of case.

13. search and replace
- replace() function.
- it replace all occurrences of the search string with the rplacement string.
example:
>>>greet = 'Hello Bob'
>>>nstr = greet.replace('Bob', 'Jane')
>>>print(nstr)
Hello Jane

14. stripping whitespace
- lstrip() remove left whitespace
- rstrip() remove right whitespace
- strip() removes both beginning and ending whitespace
example:
>>>greet = '  hello  bob  '
>>>greet.lstrip()
'hello bob  '
>>>greet.strip()
'hello bob'

15. prefixes
example:
>>>line = 'please have a nice day'
>>>line.startswith('please')
True
>>>line.startswith('p')
False

16. parsing and extracting
example:
for stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

>>>data = for stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
>>>atpos = data.find('@')
>>>print(atpos)
21
>>>sppos = data.find(' ',atpos)
>>>print(sppos)
31
>>>host = data[atpos+1,31]
>>>print(host)
uct.ac.za

*******************************************CHAPTER 7 files

1. files
- a text file can be thought of a sequence of lines.

2. open a files
- open() function
- open() returns a 'file handle' --- a variable ised to perform operations on the file.
- handle = open(filename, mode)
- returns a handle use to manipulate the file.
- filename is a string.
- mode is optional and should be 'r' if we are planning to read the file and 'w' if we
are going to write to the file.

3. what is handle ?
>>>fhand = open('mbox.txt')
>>>print(fhand)
<_10.TextIOWrapper name='mbox.txt' mode='r' encodeing='UTF-8'>

4. new line character
- use special character called the 'newline' to indicate when a line ends.
- represent it as \n in strings
- newline is one character  (a return to and start to next line)

5. file handle as a sequence
- a file handle open for read can be treated as a sequence of strings where each
line in the file is a string in the sequence.
- use for statement to iterate through a sequence.
- a sequence is an ordered set.

6. counting lines in a file.
- open a file read only.
- use a for loop to read each lines
- count the rlines and print out the number of lines.
example:
Fhand = open('mbox. txt')
count = 0
for line in fhand:
    count = count + 1
print('line count:', count)

7. reading the *whole* file
- we can read the whole file(newlines and all) into a single string.
example:
>>>fhand = open('mbox-short. txt')
>>>inp = fhand.read()
>>>print(len(inp))
94625
>>>print(inp[:20])
From stephen.marquar

8. searching through a file
- we can put an if statement in our loop to only print lines that meet some criteria.
example:
fhand = Open('mbox-short. txt')
for line in fhand :
    line = rstrip()
    if line.startwith('Form:') :
        print(line)

- we can strip the whitespace from the right-hand side of the string using rstrip()
- the newline is onsidered "white space" and is stripped

9. skippng with countinue.
- can skip a line by using the continue statement.
example:
fhand = open('mbox-short. txt')
for line in fhand:
    line = lin.rstrip()
    if not line.startwith('From:'):
        continue
    print(line)

10. using in to select Lines
- we can look for a string anywhere in a line as our selection criteria
example:
fhand = open('mbox-short. txt')
for line in fhand:
    line = line.rstrip()
    if not 'out' in line:
        continue
    print(line)

    then all lines contine 'out' will shows.

11. propt for file name
fname = input('enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startwith('sunject: ')
     count = count + 1
print('ther were', count, 'sunject lines in', fname)

12. how to deal bad names
fname = input('enter the file name: ')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startwith('sunject: ')
     count = count + 1
print('ther were', count, 'sunject lines in', fname)

*******************************************CHAPTER 8 lists

Algorithms: a set of rules or steps used to slove a problem
Data structures: a particular way of orgnizing data in a computer.

1. what is not collection?

most of variables have one value in them - when we put a new value in the variable, the old value is overwritten.

2. a list is a kind of collection

-  a collection allows us to put many values in a single 'variable'
- a collection is nice becasue we can carry many values around in one
convenient package.

example:
friends = ['Ann', 'Joe', 'Nancy']

3.List constant

- list contants are surrounded by square brackets and the elements in the list are separated by commas.
- a list element can be any python object - even another list.
- a list can be empty.

example:
>>>print([1, 24, 76])
[1, 24, 76]
>>>print(['red', 'blue', 'pink'])
['red', 'blue', 'pink']
>>>print([1, [5, 6], 9])
[1, [5, 6], 9]
>>>Print([])
[]

4.
