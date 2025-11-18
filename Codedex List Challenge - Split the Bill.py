# Split the Bill
# Lesson > arithmetic with loops

bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

total = 0

for prices in bill:
  total = total + prices

splitTotal = total/4

print(f'${round(total, 2)}')

my_share = total/4

print(f'${round(my_share, 2)}')

print(my_share)