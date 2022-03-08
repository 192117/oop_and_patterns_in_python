class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def change_map_for_lights(self, value, parametr):
        res = []
        for i in range(len(parametr)):
            for j in range(len(parametr[0])):
                if parametr[i][j] == value:
                    res.append((j, i))
        return res

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self.change_map_for_lights(1, grid)
        obstacles = self.change_map_for_lights(-1, grid)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()
