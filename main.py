alist = ["Student 1", 122, 3.45, "School Student"]
print(alist)

car_companies = ["Honda", "Toyota", "BMW", "Ford", "Tesla"]

print("First Element:", car_companies[0])
print("Second Element:", car_companies[1])
print("Last Element:", car_companies[-1])
print("List Size:", len(car_companies))

car_companies.append("Chevrolet")
print("After adding:", car_companies)

car_companies.sort()
print("After sorting in asc order:", car_companies)

car_companies.reverse()
print("After sorting in desc order:", car_companies)
