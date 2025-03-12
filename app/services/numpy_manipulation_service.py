import numpy as np 

def generate_2d_array(rows=20, cols=5, min_val=10, max_val=100):
    
    while True:
        array= np.random.randint(min_val, max_val+1, size=(rows, cols))

        for i in range(rows):
            current_row_sum = array[i].sum()
            if current_row_sum % 2 != 0:
               aux = -1 if array[i][0]>1 else 1
               array[i][0] += aux
            
        total_sum = array.sum()
        if total_sum % 5 == 0:
            break

    return array

def handle_array(array):

    div_by_3_5 = array[(array%3 == 0) & (array%5 == 0)]
    print(f'Numbers that divisible by 3 and 5:\n {div_by_3_5}')

    mean_val = np.mean(array)
    array[array>75] = mean_val

    return array

def statistics_array(array):
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





