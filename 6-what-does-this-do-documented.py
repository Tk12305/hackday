import random
import math

def process_data(data):
    """
    Processes the input data by multiplying each item with a random integer between 1 and 10,
    and then dividing by the square root of (item + 1).

    Args:
        data (list): A list of integers.

    Returns:
        list: A list of processed floating-point numbers.
    """
    result = []
    for item in data:
        temp = (item * random.randint(1, 10)) / math.sqrt(item + 1)
        result.append(temp)
    return result

def filter_data(data):
    """
    Filters the processed data to retain only even numbers greater than 50.

    Args:
        data (list): A list of floating-point numbers.

    Returns:
        list: A list of filtered numbers that are even and greater than 50.
    """
    return [x for x in data if x % 2 == 0 and x > 50]

def generate_report(data):
    """
    Generates a statistical report from the filtered data, including mean, max, min,
    variance, and standard deviation.

    Args:
        data (list): A list of floating-point numbers.

    Returns:
        dict: A dictionary containing statistical measures of the data.
    """
    report = {}
    report['mean'] = sum(data) / len(data)
    report['max'] = max(data)
    report['min'] = min(data)
    report['variance'] = sum((x - report['mean']) ** 2 for x in data) / len(data)
    report['std_dev'] = math.sqrt(report['variance'])
    return report

def complex_operation(a, b):
    """
    Performs a complex mathematical operation using two parameters.

    The operation sums up (a * i + b) / (i + 1) for i ranging from 1 to 99.

    Args:
        a (float): The first parameter, typically the mean from the report.
        b (float): The second parameter, typically the standard deviation from the report.

    Returns:
        float: The result of the complex mathematical computation.
    """
    result = 0
    for i in range(1, 100):
        result += (a * i + b) / (i + 1)
    return result

def main():
    """
    Main function to execute the data processing pipeline.

    Steps:
    1. Generates random data.
    2. Processes the data.
    3. Filters the processed data.
    4. Generates a statistical report.
    5. Performs a complex operation based on the report.
    6. Prints all results.
    """
    data = [random.randint(1, 100) for _ in range(20)]
    processed = process_data(data)
    filtered = filter_data(processed)
    report = generate_report(filtered)
    complex_result = complex_operation(report['mean'], report['std_dev'])
    print("Original Data:", data)
    print("Processed Data:", processed)
    print("Filtered Data:", filtered)
    print("Report:", report)
    print("Complex Operation Result:", complex_result)

if __name__ == "__main__":
    main()
