import random
import time
import sys
def event(event_roll,list_of_drivers): #chance that an overtake happens
    if event_roll == 1:
        driver_to_overtake = random.randint(1,len(list_of_drivers)-1)
        print("  ",list_of_drivers[driver_to_overtake],"overtakes",list_of_drivers[driver_to_overtake-1],"!!")
        time.sleep(sleep_time)
        list_of_drivers[driver_to_overtake],list_of_drivers[driver_to_overtake-1] = list_of_drivers[driver_to_overtake-1],list_of_drivers[driver_to_overtake]
        print("   End of lap order:",list_of_drivers)
        time.sleep(sleep_time)
    return list_of_drivers


def lap(current_lap,list_of_drivers):
    print("Lap",current_lap,".....................................................")
    time.sleep(sleep_time)
    event_roll = random.randint(1,2)
    list_of_drivers = event(event_roll,list_of_drivers)
    return list_of_drivers

def race(number_of_laps,list_of_drivers):
    current_lap = 1
    while current_lap <= number_of_laps:
        list_of_drivers = lap(current_lap,list_of_drivers)
        current_lap += 1
    print("Final Standings:",list_of_drivers)
    time.sleep(sleep_time)
    print("CONGRATULATIONS TO",list_of_drivers[0].upper())

list_of_drivers = ['Max Verstappen','Charles Leclerc','Lewis Hamilton','Oscar Piastri',
                   'Carlos Sainz Jr','George Russell','Sergio Perez','Fernando Alonso']
number_of_laps = 25
sleep_time = 1
print("Initial Standings:",list_of_drivers)
time.sleep(sleep_time)
print("Ready... Set... GO!!!")
time.sleep(sleep_time)
race(number_of_laps,list_of_drivers)