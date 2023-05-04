# Electron configuration
atomic_number = int(input("Enter atomic number: "))
print()

energy_level_start = 1
energy_level_end = 2

counter = 1
sub_level_name = ''
sub_level_counter = 1

current_electrons = 0
electrons = 0
electrons_distributed = False

for energy_level in range(1, 9):
    if electrons_distributed:
        break

    current_sub_level_counter = sub_level_counter  # Refresh the current counter

    for number_of_orbitals in range(energy_level_start, energy_level_end):

        difference = atomic_number - electrons

        if current_sub_level_counter == 1:
            sub_level_name = 's'

            if difference >= 2:  # Electron holding capacity of sublevel 's' is 2
                electrons += 2
                current_electrons = 2
            else:
                electrons += difference
                current_electrons = difference

        elif current_sub_level_counter == 2:
            sub_level_name = 'p'

            if difference >= 6:  # Electron holding capacity of sublevel 'p' is 6
                electrons += 6
                current_electrons = 6
            else:
                electrons += difference
                current_electrons = difference

        elif current_sub_level_counter == 3:
            sub_level_name = 'd'

            if difference >= 10:  # Electron holding capacity of sublevel 'd' is 10
                electrons += 10
                current_electrons = 10
            else:
                electrons += difference
                current_electrons = difference

        elif current_sub_level_counter == 4:
            sub_level_name = 'f'

            if difference >= 14:  # Electron holding capacity of sublevel 'f' is 14
                electrons += 14
                current_electrons = 14
            else:
                electrons += difference
                current_electrons = difference

        print(f"{number_of_orbitals}{sub_level_name}{current_electrons}", end = ' ')

        current_sub_level_counter -= 1

        if electrons == atomic_number:  # If all electrons are distributed
            electrons_distributed = True
            break   # We break the cycle and raise the flag

    if counter == 1:
        energy_level_start += 1
        energy_level_end += 1
    else:
        energy_level_end += 1
        counter = 0
    counter += 1

    if energy_level % 2 == 0:   # Increase sub_energy level every two iterations
        sub_level_counter += 1
