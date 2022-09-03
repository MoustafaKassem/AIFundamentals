# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import pdb

import util
from game import Directions

s = Directions.SOUTH
w = Directions.WEST

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """

    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
    import pdb; 
# def breadthFirstSearch(problem: SearchProblem):
    # """Search the shallowest nodes in the search tree first."""
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    from game import Directions
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    rootNode = {'state':problem.getStartState(),'cost':0};

    if  problem.isGoalState(rootNode['state']):
        return [] #no need for action we are already at the goal.

    #Nodes to be explored are called frontier
    frontier = util.Queue();
    frontier.push(rootNode);
    exploredNodes= []
    actionsToNode=[];

    while (True):
        if frontier.isEmpty():
            raise Exception("Search Failed without finding a goal");



        #print("__________________ITR________________________")
        #print("frontier")
        #print(frontier.list)

        #check for the goal


        ##else expand
        #_----#
        #pdb.set_trace();
        node = frontier.pop();
        if problem.isGoalState(node['state']):
            print ("solution is found");
            while 'action' in node.keys():
                actionsToNode.append(node['action'])
                node = node['parent']

            # print(actionsToNode)
            actionsToNode.reverse()
            return actionsToNode
        #print("Current Explored Node ");
        #print(node);
        exploredNodes.append(node['state']);
        SuccessorNodes= problem.getSuccessors(node['state']);
        #print("SuccessorNodes")
        #print(SuccessorNodes)
        #print("exploredNode")
        #print(exploredNodes)
        #pdb.set_trace();
        for nodesSuccessor in SuccessorNodes:
            childNode= {'state':nodesSuccessor[0],'action':nodesSuccessor[1],'cost':nodesSuccessor[2],'parent':node}
            #print("SuccessorNodes Created and tied to a parent")
            if childNode['state']  not in exploredNodes:
                # if problem.isGoalState(childNode['state']):
                #     print("Solution is found");
                #     print(childNode)
                #     node=childNode;
                #     while 'action' in  node.keys():
                #         #print(node['action'])
                #         actionsToNode.append(node['action'])
                #         node=node['parent']
                #
                #     # print(actionsToNode)
                #     actionsToNode.reverse()
                #     #print(actionsToNode)
                #     #pdb.set_trace();
                #
                #     return  actionsToNode
                #
                #     #actionsToNode.reverse()
                #
                # ##can be here the check of the frontier
                if childNode  not in frontier.list:
                    frontier.push(childNode)








    util.raiseNotDefined()





def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
