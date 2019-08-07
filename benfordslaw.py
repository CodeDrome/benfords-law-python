import collections


BENFORD_PERCENTAGES = [0, 0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]

def calculate(data):

    """
    Calculates a set of values from the numeric list
    input data showing how closely the first digits
    fit the Benford Distribution.
    Results are returned as a list of dictionaries.
    """

    results = []

    first_digits = list(map(lambda n: str(n)[0], data))
    first_digit_frequencies = collections.Counter(first_digits)

    for n in range(1, 10):

        data_frequency = first_digit_frequencies[str(n)]
        data_frequency_percent = data_frequency / len(data)
        benford_frequency = len(data) * BENFORD_PERCENTAGES[n]
        benford_frequency_percent = BENFORD_PERCENTAGES[n]
        difference_frequency = data_frequency - benford_frequency
        difference_frequency_percent = data_frequency_percent - benford_frequency_percent

        results.append({"n": n,
                        "data_frequency":               data_frequency,
                        "data_frequency_percent":       data_frequency_percent,
                        "benford_frequency":            benford_frequency,
                        "benford_frequency_percent":    benford_frequency_percent,
                        "difference_frequency":         difference_frequency,
                        "difference_frequency_percent": difference_frequency_percent})

    return results
