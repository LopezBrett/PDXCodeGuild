ex5_name = 'Zed A. Shaw'
ex5_age = 35 # not a lie
ex5_height = 74 # inches
ex5_weight = 180 # lbs
ex5_eyes = 'Blue'
ex5_teeth = 'White'
ex5_hair = 'Brown'
ex5_height_conversion = ex5_height * 2.5

print(f"Let's talk about {ex5_name}.")
print(f"He's {ex5_height} inches tall.")
print(f"He's {ex5_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {ex5_eyes} eyes and {ex5_hair} hair.")
print(f"His teeth are usually {ex5_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = ex5_age + ex5_height + ex5_weight
print(f"If I add {ex5_age}, {ex5_height}IN/{ex5_height_conversion}CM, and {ex5_weight} I get {total}.")
