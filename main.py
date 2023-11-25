#SAVVAS SIDERIS 40129938
import time


# create an object
class Instance:
    def __init__(self, sequence, list, value):
        self.sequence = sequence
        self.list = list
        self.value = value

    def show(self):
        print(f"{self.sequence} is {self.list} with a value of: {self.value}")

def parse_file (filename):
    start_time = time.time()
    print(f"TIME START: {start_time}")

    list_of_instances = []
    with open(filename, 'r') as file:
        for line in file:
            split_data = line.strip().split(';')
            temp_sequence = split_data[1]
            temp_list = eval(split_data[2])
            temp_value = float(split_data[3])
            temp_instance = Instance(temp_sequence, temp_list, temp_value)
            temp_instance.show()
            list_of_instances.append(temp_instance)
    end_time = time.time()
    print(f"f TIME END: {end_time}")

    elapsed = end_time - start_time
    print(f"f TIME TAKEN: {elapsed}")
    return list_of_instances


if __name__ == '__main__':
    file_name = 'C:/Users/savva/Documents/fall_2023/COEN 432/ASSIGNMENTS/ASSIGNMENT_2/A2_15000.txt'
    List_of_Instances = parse_file(file_name)
    #print(List_of_Instances) #Test if the parser did a good job

########## Simple test to check Instance creation
    #test_Instance = Instance(sequence="ACGU", list=[0, 0, 0, 0.5], value=1.5)
    #test_Instance.show()
