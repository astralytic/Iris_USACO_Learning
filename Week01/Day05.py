# Fri Jul 24, 2026

from easytello import Tello, tello

drone = tello.Tello()
flight_log = []

def log(action):
   entry = {"step": len(flight_log) + 1, "action": action}
   flight_log.append(entry)
   print(f"  [{entry['step']}] {action}")

def preflight_check():
   # print(drone.get_battery())
   # print(drone.get_temp())
   # print(drone.get_battery())
   # print(drone.get_time())
   # print(drone.get_attitude())
   return True

def fly_mission_a():
   # SmoothCurve
   for i in range(2):
       drone.curve(50, 50, 0, 80, 80, 30, 30)
       drone.curve(50, 50, 0, 20, 20, -30, 30)
       drone.cw(180)
   pass

def fly_mission_b():
   # HourGlass
   drone.go(50,50,50,30)
   drone.left(50)
   drone.go(50,0,0,30)
   drone.left(50)
   drone.up(50)
   drone.go(50,0,0,30)
   drone.up(50)
   drone.go(0,0,0,30)
   pass

def print_flight_report():
   # Loop through flight_log and print each entry
   for entry in flight_log:
       print(entry["step"], entry["action"])
   pass

#--Main--#

pilot = input("Pilot name: ")
mission = input("Mission name: ")
print(f"\nPilot {pilot} — Mission '{mission}' initializing...\n")

print("Select mission:")
print("  A -> Mission A (shape flight)")
print("  B -> Mission B (go() navigation)")
choice = input("Enter A or B: ")

if preflight_check():
   drone.takeoff()
   log("Takeoff")
   drone.wait(3)

   if choice.upper() == "A":
       fly_mission_a()
   elif choice.upper() == "B":
       fly_mission_b()
   else:
       print("Invalid choice.")

   drone.land()
   log("Land")
   drone.wait(2)

print_flight_report()
