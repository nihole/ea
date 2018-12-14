# factor determines the difference in weight between the width (y) and the depth (x)
# the larger the factor, the greater the depth affects the result (x will be greater and x less)

factor = 1.5

# List of data
a = []

# The number of examined topics
topic_number = int(raw_input("Please enter topics number: "))

# Get the data
print "Please enter the rating for each topic  one by one (0 - 10)\n"
for i in range(0, topic_number):
    a.append(float(raw_input("%s: " % str(i+1))))

# sort list
a.sort(reverse=True)

# summ numbers in the list
s = sum(a)

# for each possible y calculate the intersection area (taking into account the factor)

factor_summ = {}

for y in range(1, topic_number+1):
    # x for this y (sum should be the same)
    x = s/(y)

    
    factor_summ[y] = 0

    for j in range(0, y):
        if a[j] > x:
            factor_summ[y] = factor_summ[y] + x**factor
        else:
            factor_summ[y] = factor_summ[y] + a[j]**factor

# find y with maximum factor_summ
y_result = max(factor_summ, key=factor_summ.get)


# find x for this y
x_result = s/y_result

# x result should not be greater then the maximum assessment
if x_result > a[0]:
    x_result = a[0]
    # The area should be equal to the sum of all estimates.

    y_result = s/x_result


# We have to use 10 point scale for the output
print "x = %s, y = %s" % (int(round(x_result)), int(round(10*y_result/topic_number)))
