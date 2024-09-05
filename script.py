from time import time

start_time = time()


def find_kaprekar_sum(num):
    digit_sum = 0
    seen_numbers = set()
    while num not in seen_numbers:
        seen_numbers.add(num)
        digits = [int(x) for x in str(num)]
        sort_asc = int("".join(map(str, sorted(digits))))
        sort_desc = int("".join(map(str, sorted(digits, reverse=True))))
        num = sort_desc - sort_asc
        digit_sum = sum(int(x) for x in str(num))
    seen_control.update(seen_numbers)
    return digit_sum


digits = 3

while digits < 10:
    n = 10 ** (digits - 1)
    upper_bound = (10**digits) - 2
    seen_control = set()
    found_sums = []

    while n < upper_bound:
        if len(set(str(n))) < digits:
            n += 1
            continue

        if n not in seen_control:
            kaprekar_sum = find_kaprekar_sum(n)
            if kaprekar_sum and kaprekar_sum not in found_sums:
                found_sums.append(kaprekar_sum)
        n += 1

    if len(found_sums) > 1:
        print(f"Digits: {digits} | Sums: {', '.join(map(str, found_sums))}")
    else:
        print(f"Digits: {digits} | Sum: {found_sums[0]}")
    digits += 1

end_time = time()
total_time = end_time - start_time
print(f"Total execution time: {total_time:.4f} seconds")
