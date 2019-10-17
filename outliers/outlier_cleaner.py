#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    errors = [abs(pred - net_worth) for pred, net_worth in zip(predictions, net_worths)]
    data = zip(ages, net_worths, errors)
    data.sort(key=lambda tup: tup[2])  # sort by error
    new_length = int(len(predictions) * 0.9)  # set the new length without the last 10%
    cleaned_data = data[:new_length]   # trim the array

    return cleaned_data

