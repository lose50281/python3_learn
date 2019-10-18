import function
import sys

try:
    function.searchrecord(sys.argv[1])

except IndexError:
    function.addrecord(sys.argv[1])