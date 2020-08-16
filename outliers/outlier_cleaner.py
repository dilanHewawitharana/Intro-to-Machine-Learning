#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    error = (predictions - net_worths)*(predictions - net_worths)
    
    final_array = np.concatenate((ages,net_worths,error), axis=1)
    
    final_array = sorted(final_array, key = lambda t:t[2] )
    limit = len(ages)*0.9
    
    cleaned_data = final_array[0:int(limit)]

    return cleaned_data

