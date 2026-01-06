import math
def wind_chill(t,v):
  wind=35.74+0.6215*t+(0.4275*t-35.74)*math.pow(v,0.16)
t=float(input("Enter temperature(F):"))
v=float(input("Enter wind speed(mph):"))
print("wind chill=",wind_chill(t,v))