import random

def pad(literal):
    if not literal:
        return "  \n  "
    lines = ['', *literal.splitlines(), '']
    width = max(len(line) for line in lines)
    return '\n'.join(' ' + line.ljust(width) + ' ' for line in lines)

def generate_random_grid():
  marks = ['#', ' ']
  lines = []
  for line_id in range(3):
    lines.extend([marks[random.randint(0,1)] for x in range(10) ])
    lines.append('\n')
  return "".join(lines)


RANDOM = pad(generate_random_grid())


BLOCK = pad("""\
##
##
""")

BLINKER = pad("""\

###

""")

BLINKER3 = pad("""\
     #
###  # ###
     #
""")

PULSAR = pad("""\
  ###

#    #
#    #
#    #
  ###
""")

PENTADECATHLON = pad("""\
  #  #    # #
###  ###### ###
  #  #    # #
""")

PINWHEEL = pad("""\
 ####
#  # #
##   #
# #  #
#    #
 ####
""")

GLIDER = pad("""\
 #
  #
###
""")

DIEHARD = pad("""\
      #
##
 #   ###
""")

GLIDER_GUN = pad("""\
                        #
                      # #
            ##      ##            ##
           #   #    ##            ##
##        #     #   ##
##        #   # ##    # #
          #     #       #
           #   #
            ##
""")

PENTOMINO = pad("""\
 ##
##
 #
""")

BASELINE = pad("""\
######## #####   ###      ####### #####
""")



PATTERNS = [
    'BLOCK', 'BLINKER', 'BLINKER3', 'PULSAR', 'PENTADECATHLON', 'PINWHEEL', 'GLIDER', 'DIEHARD', 'GLIDER_GUN',
    'PENTOMINO'
]

__all__ = PATTERNS[:]
