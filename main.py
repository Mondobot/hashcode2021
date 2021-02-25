
# class Ingredient:

#     def __init__(self, name):
#         # super().__init__()

#         self.name = name
#         self.pizzas = []
#         self.yes = None
#         self.no = None

#     def insert(self, name):
#         self.yes = Ingredient()


def getFileContents(filepath):
    f = open(filepath, 'r')
    
    line = f.readline()
    values = line.split()

    values = {'time': int(values[0]), 'intersections': int(values[1]), 'streets': int(values[2]), 'cars': int(values[3]), 'points': int(values[4])}

    intersections = []
    cars = []

    for i in range(values['streets']):
        line = f.readline()
        line = line.split()
        intersections.append({'start': line[0], 'end': line[1], 'name': line[2], 'length': int(line[3])})

    for i in range(values['cars']):
        line = f.readline()
        line = line.split()
        cars.append({'streets': int(line[0]), 'route': line[1:]})

    f.close()
    
    return values, intersections, cars

def writeResult(filepath, nrOfIntersections, intersections):
    f = open(filepath, "w")

    f.write("{}\n".format(nrOfIntersections))

    for i in range(nrOfIntersections):
        f.write("{}\n".format(intersections[i]['id']))
        f.write("{}\n".format(intersections[i]['incomingStreets']))
        for j in range(intersections[i]['incomingStreets']):
            f.write("{} {}\n".format(intersections[i]['streets'][j]['name'], intersections[i]['streets'][j]['greenTime']))


values, intersections, cars = getFileContents('a.txt')

print(values)
print(intersections)
print(cars)




















'''
nrOfIntersections = 3
intersections = []

intersections.append({'id': '1', 'incomingStreets': 2, 'streets': [{'name': 'rue-d-athenes', 'greenTime': 2}, {'name': 'rue-d-amsterdam', 'greenTime': 1}]})
intersections.append({'id': '0', 'incomingStreets': 1, 'streets': [{'name': 'rue-de-londres', 'greenTime': 2}]})
intersections.append({'id': '2', 'incomingStreets': 1, 'streets': [{'name': 'rue-de-moscou', 'greenTime': 1}]})
# Do something

writeResult("result.txt",nrOfIntersections,intersections)
'''
