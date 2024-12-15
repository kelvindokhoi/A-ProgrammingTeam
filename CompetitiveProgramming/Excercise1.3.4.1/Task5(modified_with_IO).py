# print the day of the week of a given date and calculate time passed
from datetime import date
import os

def get_absolute_path(filename):
  current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
  return os.path.join(current_dir, filename)


def write_to_file(output_data, filename=get_absolute_path("out.txt")):
    with open(filename, "w") as f:
        f.write("\n".join(output_data))

def read_from_file(filename=get_absolute_path("in.txt")):
    with open(filename, "r") as f:
        return f.read().splitlines()

def compare_output(output_data, sample_output_file=get_absolute_path("sample_output.txt")):
    with open(sample_output_file, "r") as f:
        sample_output = f.read().splitlines()
    return output_data == sample_output

def sortbirth(birthdates):

    today = date.today()

    def sortpara(indiv):
        day, month, year = map(int,indiv.split())
        obj_date = date(year,month,day)
        age = today.year - obj_date.year - ((today.month,today.day)<(obj_date.month,obj_date.day))
        return obj_date.month, obj_date.day, age
    
    return sorted(birthdates,key=sortpara)

input_data = read_from_file()
output_data = sortbirth(input_data)


write_to_file(output_data)

if compare_output(output_data):
  print("Output matches sample output.")
else:
  print("Output differs from sample output.")


