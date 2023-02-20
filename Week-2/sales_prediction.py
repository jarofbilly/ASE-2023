sales = float(input('Projected total sales: '))

for x in range(1, 11):
    profit = round(sales * 0.23, 2)
    print(f'Projected profit for Year {x}: {profit:016}')
    sales *= 1.05
