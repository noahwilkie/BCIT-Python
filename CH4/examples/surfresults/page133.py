highest_score = 0
result_f = open("results.txt")
scores = []

for line in result_f:
    (name, score) = line.split()
    scores.append(score)
    print(scores)

result_f.close()

scores.sort()
scores.reverse()

print(scores)
print()
print("The highest score was: ", scores[0])
print("The 2nd highest score was: ", scores[1])
print("The 3rd highest score was: ", scores[2])
print()