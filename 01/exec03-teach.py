num = 0
count = 0
input_str = raw_input('input a number: ')

while input_str:
    num = num + float(input_str)
    count += 1.0
    input_str = raw_input('input a number: ')

print num / count
