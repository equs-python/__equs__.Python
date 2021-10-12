def convex_combs(collection, n_terms):
    base = len(collection)

    for i in range(base ** (n_terms - 1), base ** n_terms):

        current_combination = []
        integer_rep = i

        current_power = 1
        while current_power <= n_terms:
    
            current_combination.append(
                collection[
                    int(integer_rep % (base ** current_power) // (base ** (current_power - 1))
                )])

            integer_rep -= integer_rep % (base ** current_power)
            current_power += 1
        yield current_combination

for i in convex_combs([1, 2, 3], 2):
    print(i)

