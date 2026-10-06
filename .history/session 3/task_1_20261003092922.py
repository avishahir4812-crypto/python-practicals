cricket_scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = []

for score in cricket_scores:
    rounded_scores.append(round(score))

print("Original list:", cricket_scores)
print("Rounded list:", rounded_scores)