class Grid():
    def __init__(self, dimensions: tuple):
        self._dimensions =  dimensions
    
    def print_grid(self):
        rows, columns = self._dimensions[0], self._dimensions[1]
        # print(rows, columns)
        for _ in range(rows):
            print("[ ]"* columns)
    
def user_input_dimensions():
    # Ask the user the dimensions wanted
    user_defined_dimensions = \
        input("Input dimensions wanted (e.g. 3x3, 5x5): ")
    # Clean up the input
    user_defined_dimensions = user_defined_dimensions.replace("x", "")
    # Make it a tuple e.g. (3,3)
    x, y = int(user_defined_dimensions[0]), int(user_defined_dimensions[1])
    user_defined_dimensions = x,y                                         
    
    return user_defined_dimensions
 
dimensions = user_input_dimensions()
print(dimensions)

new_grid = Grid(dimensions=dimensions)
new_grid.print_grid()