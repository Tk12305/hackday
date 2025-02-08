import random
import math

def process_data(data):
    result = []
    for item in data:
        temp = (item * random.randint(1, 10)) / math.sqrt(item + 1)
        result.append(temp)
    return result

def filter_data(data):
    return [x for x in data if x % 2 == 0 and x > 50]

def generate_report(data):
    report = {}
    report['mean'] = sum(data) / len(data)
    report['max'] = max(data)
    report['min'] = min(data)
    report['variance'] = sum((x - report['mean']) ** 2 for x in data) / len(data)
    report['std_dev'] = math.sqrt(report['variance'])
    return report

def complex_operation(a, b):
    result = 0
    for i in range(1, 100):
        result += (a * i + b) / (i + 1)
    return result

def main():
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
