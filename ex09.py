#Palindrome
def Palindrome(word):
  reversedWord = ""
  for i in range(len(word)-1, -1, -1):
    reversedWord +=word[i]
  if reversedWord == word:
    return True
  else:
    return False

word = str(input("Enter word to check if it is Palindrome: "))
print(Palindrome(word))


#Smart home
#1
light_status = {"Kitchen":"On",
                "Living_room":"Off",
                "Office":"On",
                "Hall":"On",
                "Bathroom":"Off",
                "Bedroom":"Off", }

#2
def light_press(room_name):
    if room_name in light_status:
        if light_status[room_name] == "Off":
            light_status[room_name] = "On"
        else:
            light_status[room_name] = "Off"
        return light_status[room_name]
    else:
        return("There is no such room!")

room_name = str(input("Enter name of room: "))
print(light_press(room_name))

#3
def check_lights_on():
    lights_on = [room for room, status in light_status.items() if status == "On"]
    print("Lights are switched on in the ", ", ".join(lights_on), end=".\n" )

check_lights_on()

#4
def lights_off():
    for room, status in light_status.items():
        if status == "On":
            light_status[room] = "Off"

lights_off()
print(light_status)

#5
def cost(power, price, *seconds):
    consumed_energy = 0
    for s in seconds:
        consumed_energy += ((power * (s / 3600)) / 1000) * price
    return consumed_energy

print(cost(3,0.5,9000))
print(cost(3,0.9,9000))
print(cost(3,2.0,9000))