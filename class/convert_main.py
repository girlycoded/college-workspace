from convert import cel_tor_far, far_to_cel
from pprint import pprint

temp = float(input("Enter a temperature in celsius "))
temps = {
    "degrees_in_farenheit": cel_tor_far(temp), 
    "degrees_in_celsius": far_to_cel(temp)
}

pprint(temps)