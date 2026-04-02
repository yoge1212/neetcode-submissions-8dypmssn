class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #there are n cars traveling to the same destination on a one-lane highway

        #we are given two arrays of integers (position and speed) (both are of length n)
        #the destination is at position target miles

        #rules:
        #a car can not pass another car ahead of it. it can only catch up to another car and then dirve at thes mae speed as the car ahead of it
        #a car fleet is a non-empty set of cards drive at the smae postiion and same speed
        #a single car is also consdiered a car fleet
        #if a car catches up to a car fleet, the moment the fleet reaches the destination then,
        #the car is considered to be part of the fleet. 
        #we need to find and return the number of different car feets that will arrive at the destination
        
        #Input: target = 10, position = [1,4], speed = [3,2]

        #car 1: (pos 1, speed 3)
        #car 2: (pos 4, speed 2)
        # (10 - 1) = 9 miles away / 3 = 3
        #car 2: (10 - 4) = 6 miles away / 2 = 3
        #so they will reach at the same time

        #[(4, 2), (1, 2), (0, 1) , (7, 1)]

        #(0, 1),(1, 2), (4, 2), (7, 1)
        #[[(7, 1), (4,2)], (1, 2), (0, 1)]

        #first we need to create a new array that has both a cars pos and speed in descending order
        #then we create a stack that will help us create car fleets
        #for every car in our new car we pop from the stack, we check to see if the car in that arrives at the same time,
        #if it does add it to that smae inner array
        #if it doesnt add it seperately

        car_pos_speed = list(zip(position, speed))
        
        car_pos_speed.sort(reverse=True)

        stack = []

        for car in car_pos_speed:
            if stack:
                latest = stack[-1]
                if not self.arriving_same_time(target, latest, car):
                    stack.append(car)
            else:
                stack.append(car)

        return len(stack)

    
    def arriving_same_time(self, target: int, car1: tuple, car2: tuple) -> bool:

        car1_time = (target - car1[0])/car1[1]
        car2_time = (target - car2[0])/car2[1]

        return car1_time >= car2_time


