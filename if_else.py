
import math
import os
import random
import re
import sys

n = int(input().strip())

if(n % 2 != 0):
    print("Weird")
if(n %2 == 0 and(n <= 5 and n>=2)):
    print("Not Weird")   
if(n %2 == 0 and(n <= 20 and n>=6)):
    print("Weird")
if(n %2 == 0 and n >20):   
    print("Not Weird")    
