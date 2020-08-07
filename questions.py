valve_pressure = 10
try:
  PRESSURE_VALUE += 5
  print("still working")
except NameError:
  print("A NameError was generated!")

