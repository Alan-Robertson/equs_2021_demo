def convex_combs(collection:list, n_terms:int) -> list:
    '''
        convex_combs
        A generator that produces convex combinations
        :: collection : list :: A list of objects to take combinations of
        :: n_terms    : int  :: The number of objects in the combination
        No elements of the collection are modified
        Yields combinations
    '''
    base = len(collection)

    if n_terms <= 0:
        return

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


if __name__ == '__main__':
    for i in convex_combs([1, 2, 3], 2):
        print(i)
