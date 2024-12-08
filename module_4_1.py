from fake_math import divide as zero
from true_math import divide as inf

result1 = zero(69, 3)
result2 = zero(3, 0)
result3 = inf(49, 7)
result4 = inf(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)