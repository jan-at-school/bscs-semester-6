'''
8 puzzle problem, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.
States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the state (string):
'1-2-3
 4-5-6
 7-8-e'
will become (in lists):
[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]
'''
from timeit import default_timer as timer
from simpleai.search import *
# from simpleai.search import SearchProblem, breadth_first, depth_first,   limited_depth_first, iterative_limited_depth_first, uniform_cost

'''
SearchProblem, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost'''


GOAL = 'Bucharest'

INITIAL = 'Arad'

mapGraph = {
    'Oradea': {
        'Zerind': 71,
        'Sibiu': 151
    },
    'Zerind': {
        'Arad': 75,
        'Oradea': 71
    },
    'Arad': {
        'Zerind': 75,
        'Sibiu': 140,
        'Timisoara': 118
    },
    'Timisoara': {
        'Arad': 118,
        'Lugoj': 111
    },
    'Sibiu': {
        'Oradea': 151,
        'Fagaras': 99,
        'Arad': 140,
        'Rimnicu Vilcea': 80
    },
    'Fagaras': {
        'Sibiu': 99,
        'Bucharest': 211
    },
    'Rimnicu Vilcea': {

        'Sibiu': 80,
        'Pitesti': 97,
        'Craiova': 146
    },
    'Lugoj': {

        'Timisoara': 111,
        'Mehadia': 70
    },
    'Pitesti': {
        'Bucharest': 101,
        'Rimnicu Vilcea': 97,
        'Craiova': 138
    },
    'Mehadia': {
        'Lugoj': 70,
        'Drobeta': 75
    },
    'Drobeta': {
        'Mehadia': 75,
        'Craiova': 120
    },
    'Craiova': {
        'Pitesti': 138,
        'Rimnicu Vilcea': 146,
        'Drobeta': 120
    },
    'Bucharest': {
        'Fagaras': 211,
        'Pitesti': 101
    },
}


class EigthPuzzleProblem(SearchProblem):
    def actions(self, state):
        print(list(mapGraph[state].keys()))
        return list(mapGraph[state].keys())

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        print('Next State: ',action)
        return action

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        return state == GOAL

    def cost(self, state1, action, state2):
        '''Uniform cost
        '''
        

        # print(state1, state2)
        return mapGraph[state1][state2]


# Breadth First
start = timer()
result = iterative_limited_depth_first(
    EigthPuzzleProblem(INITIAL),graph_search=True)
end = timer()

# Time
print('Time: ' + str(end - start))

# cost of solution
print(result.cost)

# Solution
for action, state in result.path():
    
    print(state)
