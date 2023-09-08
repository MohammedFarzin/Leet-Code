def generate(num_rows:int):
    if num_rows == 0:
        return []
    
    triangle = [[1]]

    for i in range(1, num_rows):
        prev_row = triangle[-1]
        new_row = [1]
        
        prev_len = len(prev_row)
        for j in range(1, len(prev_row)):
            first = prev_row[j-1]
            second =  prev_row[1]
            new_row.append(prev_row[j-1] + prev_row[1])

generate(5)