cars_count = 0
car_list = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for i, car in enumerate(car_list):
    print('я езжу на автомобиле марки ', car)
    if i == 0:
        continue
    else:
        cars_count += 10
        print(cars_count)