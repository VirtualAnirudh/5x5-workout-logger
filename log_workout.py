#!/usr/bin/env python3

# Workout A 
# Squats (5x5)
# Bench Press (5x5)
# Barbell Rows (5x5)

# Workout B
# Squats (5x5)
# Overhead Press (5x5)
# Deadlift (1x5)

import sys

# TODO: Log Workouts to a csv file
def log_workout(date, workout, weights):
    print(date, workout, weights)


date = sys.argv[1]
workout = sys.argv[2]
weights = [int(x) for x in sys.argv[3:]]

log_workout(date, workout, weights)


