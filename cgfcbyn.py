original = "('Employees',)"
print(original)
removed = original.replace("(", "")
removed1 = removed.replace("'", "")
removed2 = removed1.replace(",", "")
removed3 = removed2.replace(")", "")
print('####################################')
print(removed3)
