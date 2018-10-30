scores = {}
result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()

print("The highest scores were:")
for each_score in sorted(scores.keys(), reverse=True):
    print("Surfer " + scores[each_score] + " scored " + each_score)
print()
for score, surfer in sorted(scores.items(), reverse=True):
    print(surfer + " had a score of " + str(score))
