def arithmetic_arranger(problems,cond=False):
#----------------------assigning variables----------------------
  import re
  op = ["+", "-"]
  split_by_operators = []
  arranged_problems = ""
  top = ""
  middle = ""
  bottom = ""
  first = []
  sign = []
  second = []
  sums = ""
  line = ""

#--------------eliminate all spaces inside the elements -----------
  alist = [x.replace(' ', '') for x in problems]

#--------------------max 5 math problems condition ----------------
  if len(alist) > 5:
    arranged_problems = "Error: Too many problems."
  else:
#----split the list of math problems into pieces of first operand, sign, second operand using regex; didn't want to use spaces to split because it's not dinamic-----------------------------------------------------
      for i in range(len(alist)):
        split_by_operators = [re.findall('\w+|\W+', i) for i in alist]

#--------------------- only digits condition ----------------------
      for i in split_by_operators:
        first = i[0]
        sign = i[1]
        second = i[2]
        if not first.isdigit() or not second.isdigit():
          return 'Error: Numbers must only contain digits.'

#------------------ allowed operators condition --------------------
        if sign not in op:
          return "Error: Operator must be '+' or '-'."
#----------------- numbers length max 4 condition -------------------
        elif len(first) > 4 or len(second) > 4:
          return "Error: Numbers cannot be more than four digits."
#------------------- compiling the operations -----------------------
        max_length = max(len(first), len(second))+2
        spc = " "
        middle += str(sign + second.rjust(max_length-1))
        top += str(first.rjust(max_length))
        line += str("-"*max_length)
        if sign == '+':
          sums = int(i[0]) + int(i[2])
        elif sign == '-':
          sums = int(i[0]) - int(i[2])
        bottom += str(sums).rjust(max_length)

        if len(first)-1 <= len(alist):
            top += 4*spc
            middle += 4*spc
            line += 4*spc
            bottom += 4*spc
        if cond == True:
          arranged_problems = top.rstrip(spc) + "\n" + middle.rstrip(spc) + "\n" + line.rstrip(spc) + "\n" + bottom.rstrip(spc)
        else:
          arranged_problems = top.rstrip(spc) + "\n" + middle.rstrip(spc) + "\n" + line.rstrip(spc)

      # print(arranged_problems)
  return arranged_problems
