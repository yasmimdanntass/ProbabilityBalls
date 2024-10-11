import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []  
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, number):
        if number >= len(self.contents):
         
            drawn_balls = self.contents[:]
            self.contents.clear()  
            return drawn_balls
        
        balls_drawn = []
        for _ in range(number):
            ind = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents[ind])
            self.contents.pop(ind)  

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
       
        hat_copy = copy.deepcopy(hat)
        
    
        drawn_balls = hat_copy.draw(num_balls_drawn)

  
        drawn_ball_counts = {color: drawn_balls.count(color) for color in expected_balls}

        if all(drawn_ball_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            success_count += 1

    probability = success_count / num_experiments
    return probability
