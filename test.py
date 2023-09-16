
attacker, draw, defender = 0, 0, 0
sample_space_attacker = [sorted([x, y, z], reverse=True)[:2] for x in range(1, 7)
                         for y in range(1, 7) for z in range(1, 7)]
sample_space_defender = [sorted([x, y], reverse=True) for x in range(1, 7)
                         for y in range(1, 7)]
for x in range(len(sample_space_attacker)):
    for y in range(len(sample_space_defender)):
        score = 0
        for i, j in zip(sample_space_attacker[x], sample_space_defender[y]):
            if i > j:
                score += 1
            else:
                score -= 1
        if score > 0:
            attacker += 1
        elif score == 0:
            draw += 1
        else:
            defender += 1
print(attacker / (6**5))
print(draw / (6**5))
print(defender / (6**5))
