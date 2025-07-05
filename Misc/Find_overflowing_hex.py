num1 = 0xE73E83A82F7B6948
num2 = 0x7CFB8DDC6FA6FB98
op = 'sub'

# Perform operation
if op == 'add':
    result = num1 + num2
else:  # op == 'sub'
    result = num1 - num2  # Match sub r11, r12

# Ensure 64-bit unsigned result (handles negative numbers via two's complement)
result = result & 0xFFFFFFFFFFFFFFFF

# Format as 16-digit uppercase hex with '0x' prefix
newnum = f'0x{result:016X}'

print(newnum)