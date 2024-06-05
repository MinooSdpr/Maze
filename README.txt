The task is to find route in a maze from Start to the Goal by using the A* algorithm and BFS. we can move left, down, right, up but it cannot move diagonally. 
It also cannot enter the filled cells or move out of the maze. Path cost is the number of agent moves. 
Heuristic function defined as the Euclidean distance from the current position to the target position. 
Maze is provided in an input text file as a matrix where the starting position is indicated by "S", the target position is indicated by "G", the walls are indicated by "%" and the empty positions that the robot can move to indicated by " ". 
In output, the path traveled by the robot is marked with ".".