n = int(input())
S = input()

result = ""

for c in S:
    result = result + chr(abs(((ord(c) + n - ord('A')) % 26)) + ord('A'))

print(result)
