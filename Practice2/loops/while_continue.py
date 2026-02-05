i = 0
while i < 5:
    i += 1 # most important thing is the counter must be before continue because it skips everything below it and starts loop again thus the loop becomes infinite
    if i == 3:
        continue
    print(i)
