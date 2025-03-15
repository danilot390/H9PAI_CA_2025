import numpy as np 

def generate_2d_array(rows=20, cols=5, min_val=10, max_val=100):
    """
    Generate a 2D matrix using NumPy take into account that parameters rows, cols, min value and max value (default 20, 5, 10 and 100)
    Return:
        NumPy array that follow given parameters.
    """
    while True:
        array= np.random.randint(min_val, max_val+1, size=(rows, cols))

        for i in range(rows):
            current_row_sum = array[i].sum()
            if current_row_sum % 2 != 0:
               aux = -1 if array[i][0]>10 else 1
               array[i][0] += aux
            
        total_sum = array.sum()
        if total_sum % 5 == 0:
            break

    return array

def handle_array(array):
    """
    Indentify and print in the terminal the numbers that are divisible by 3 and 5, and update values greater than 75 by the array's mean.
    Return:
        Array that reflect updated values.
    """
    div_by_3_5 = array[(array%3 == 0) & (array%5 == 0)]
    print(f'Numbers that divisible by 3 and 5:\n {div_by_3_5}')

    mean_val = np.mean(array)
    array[array>75] = mean_val

    return array

def statistics_array(array):
    """
    Display key insights such as mean, standard deviation, median of the array and vaciance for each column.
    Return:
        dict that contains mean, standard deviation, and mean of the array, and variance per column.
    """
    mean_array = np.mean(array)
    stand_deviation_array = np.std(array)
    median_array = np.median(array)
    variance_columns = np.var(array, axis=0)

    stats = {
        'mean': mean_array,
        'stand_deviation': stand_deviation_array,
        'median': median_array,
        'variance per column': variance_columns.tolist(),
    }
    
    return stats 





