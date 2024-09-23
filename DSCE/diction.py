system_developers = {'Digit':25, 'Dylan':22, 'Mr-AI':24, 'Carnivore':20, 'Thug':21}
print(f"System Developers: \n{system_developers}")

gui_developer = system_developers.update({'Carnivore':23})
print(f"GUI Developer: {gui_developer}")

def get_developers_Name():
    dev_names = system_developers.keys()
    return f"Developer Names: {dev_names}"

def get_developers_Age():
    dev_age = system_developers.values()
    return f"Developers Age: {dev_age}"

system_developers.pop('Thug')

print(get_developers_Name())
print(get_developers_Age())

copyDevs = system_developers.copy()
print(copyDevs.items())

copyDevs.clear()

if 'Zed' not in system_developers.values():
    print(True)