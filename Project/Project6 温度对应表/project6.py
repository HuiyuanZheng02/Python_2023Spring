'''
2023-04-13
@HuiyuanZheng02
'''

def c2f_temperature(celsius):
    """
    This function takes in a temperature in Celsius and returns the temperature in Fahrenheit using the formula:
    fahrenheit = 9 celsius/5 + 32
    """
    fahrenheit = 9/5 * celsius + 32
    return fahrenheit

def main():
    celsius_degrees = list(range(-20, 45, 5))  # Create a list of Celsius temperatures from -20 to 40 with a step of 5 degrees.
    fahrenheit_degrees = [c2f_temperature(celsius) for celsius in celsius_degrees]  # Use list comprehension to generate a new list of Fahrenheit temperatures corresponding to each Celsius temperature in the celsius_degrees list.
    
    # Print the temperature table with three columns: #, Celsius, Fahrenheit
    print(f"{'#':<5}{'celsius':>10}{'fahrenheit':>15}")
    for i in range(len(celsius_degrees)):
        print(f"{i+1:<5}{celsius_degrees[i]:>10.1f}{fahrenheit_degrees[i]:>15.1f}")

if __name__ == '__main__':
    main()