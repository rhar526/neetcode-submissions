class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = []

        for i, p in enumerate(position):
            cars.append([p, speed[i]])
        
        descSortedCars = (sorted(cars))[::-1]
        print(descSortedCars)

        for car in descSortedCars:
            pos = car[0]
            speed = car[1]

            time = (target - pos)/speed
            car.append(time)

            if not stack or stack[-1][2] < car[2]:
                stack.append(car)
    
            
        return len(stack)