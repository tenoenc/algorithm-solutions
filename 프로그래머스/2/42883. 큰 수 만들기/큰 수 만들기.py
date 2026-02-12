def solution(number, k):
	stack = []
	i = 0

	for num in number:
		while k > 0 and stack and num > stack[-1]:
			stack.pop()
			k -= 1
		stack.append(num)
		i += 1

	if k > 0:
		stack = stack[:-k]

	return ''.join(stack)