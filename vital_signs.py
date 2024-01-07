pulse_rate = int(input("Enter your pulse rate: "))
heart_beat_rate = int(input("Enter your heartbeat rate: "))
print("Enter Blood Pressure: \n")
systolic_pressure = float(input("Enter your systolic pressure: "))
diastolic_pressure = float(input("Enter your diastolic pressure: "))
temperature = int(input("Enter your temperature: "))
try:
    if (60 <= pulse_rate <= 90) and (60 <= heart_beat_rate <= 90) and (temperature == 37.0):
          if (systolic_pressure >= 90 and systolic_pressure <= 120) and (diastolic_pressure >= 60 and diastolic_pressure <= 80):
                    print("Blood Pressure is Normal")
          else:
                    print("Blood Pressure is Abnormal")
          print("Vital Sign Normal")
        
    elif (pulse_rate == 40) and (heart_beat_rate == 55) and (temperature == 37.0):
        print("Vital Sign Critical!")
    else:
        print("Life function critical")
except ValueError:
    print("Enter a number")


'''
 Normal Vital Signs: > Pulse-(60-99perminute) > haert rate-(60-99perminute) >bloodpressure-(120/80) > temperature-37.0
 '''        