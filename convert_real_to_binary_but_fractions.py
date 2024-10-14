# tbh it's easiest than expected
# algorithm from #0 to-do-list from University of Wrocław (Computer Science) 

# enter:
# a -> real number, belongs to [0, 1)
#
# exit:
# result -> our result

a = 0.375 # f.i. 0.375

print(0)
print(".")
while a != 0:
    a *= 2
    print(a//1)
    a = a%1
