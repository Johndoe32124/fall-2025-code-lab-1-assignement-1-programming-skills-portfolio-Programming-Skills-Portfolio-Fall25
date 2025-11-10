#Exercise 7
def Count(Min, Max, Increment):
	print(list(range(Min, Max + Increment, Increment)))

Count(0, 50, 1) 
# from 0 to 50 by increments of 1
Count(50, 0, -1)
# from 50 to 0 by increments of -1 
Count(30, 50, 1)
# from 30 to 50 by increments of 1
Count(50, 10, -2)
# from 50 to 10 by increments of -2
Count(100, 200, 5)
# from 100 to 200 by increments of 5

#Done on October 8th