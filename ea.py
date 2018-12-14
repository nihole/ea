factor = 1.5
a = []

# The number of parameters
par_number = int(raw_input("Please enter parameters number: "))

# Get the data
print "Please enter the values one by one\n"
for i in range(0, par_number):
    a.append(float(raw_input("%s: " % i)))

# sort list
a.sort(reverse=True)

# summ numbers in the list
s = sum(a)

# for each possible y calculate the intersection area

factor_summ = {}

for y in range(1, par_number+1):
    # x for this y (sum should be the same)
    x = s/(y)

    
    factor_summ[y] = 0

    for j in range(0, y):
        if a[j] > x:
            factor_summ[y] = factor_summ[y] + x**factor
        else:
            factor_summ[y] = factor_summ[y] + a[j]**factor

# find y with maximum sum
y_result = max(factor_summ, key=factor_summ.get)

# find x for this y
x_result = s/y_result

if x_result > a[0]:
    x_result = a[0]
    y_result = s/x_result


print "x = %s, y = %s" % (int(round(10*x_result/par_number)), int(round(10*y_result/par_number)))
