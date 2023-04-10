# In the 2-D world of Flatland, the Circles were having their sports day and wanted to end it with a nice formation. So, they called upon Mr. Sphere from Spaceland for help. Mr Sphere decides to arrange the Circles in square formations. 
# He starts with N Circles and forms the largest possible square using these Circles. He then takes the remaining Circles and repeats the procedure.
# A square of side S requires S2 Circles to create.Find the number of squares he will be able to form at the end of the process.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for _ in range(int(input())):
    n = int(input())
    sq = 0
    while n >= 1:
        sr = int(n**.5)
        sq += 1
        n -= sr**2
    print(sq)
