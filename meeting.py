meets = [(1, 5), (2, 8), (5, 7), (10, 12)]
meets_sorted = sorted(meets, key=lambda x: x[1])
print(meets_sorted)

print(meets_sorted[0])

finish_time = meets_sorted[0][1]
for meet in meets_sorted[1:]:
   if meet[0] >= finish_time: 
       finish_time = meet[1]
       print(meet)

