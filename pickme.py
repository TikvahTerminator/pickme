import pickle
import sys

unpic = pickle.load(open(sys.argv[1],'rb'))

for arr in unpic:
   line = ''
   for tup in arr:
       line += tup[0] * tup[1]
   print line
