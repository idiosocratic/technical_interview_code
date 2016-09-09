# technical interview exercises

"""Question 1: Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = “udacity” and t = “ad”, then the function returns True. Your function definition should look like: “question1(s, t)”, and return a boolean True or False."""

def question1(s, t):
    if len(t) > len(s):
        print "Substring not possible!"
        return False
    char_list = []
    for char in s:
        char_list.append(char)
    for char1 in t:
        found = False
        pop_index = None
        for index, char2 in enumerate(char_list):
            if char1 == char2:
                found = True
                pop_index = index
        if found == False:
            print "Missing letter! Anagram not possible!"
            return False
        popped = char_list.pop(pop_index)
    print "Anagram possible!"
    return True


"""Question 2: Given a string a, find the longest palindromic substring contained in a. Your function definition should look like "question2(a)", and return a string."""

def question2(a):
    
    base_len = len(a)
    
    search_len = base_len # initialize
    
    while search_len > 1:

        iter = base_len - search_len
        
        for i in range(iter + 1):

            search_substring = a[i:search_len+i]

            if search_substring == search_substring[::-1]:

                return search_substring

        search_len -= 1

    if search_len == 1:

        return "Only trivial palindrome exists, pick any character."



"""Question 3: Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this: {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}. Vertices are represented as unique strings. The function definition should be "question3(G)" """

def question3(G):
    
    # reformatting our graph will allow for easier data manipulation
    reformated_graph = []
    
    for vertex_key in G:
    
        for neighbor in vertex_key:
    
            vertex_pair = (sorted([ vertex_key, neighbor[0] ]), neighbor[1])
            
            vertex_pair_present = False
                           
            for entry in reformated_graph:
                           
                if entry[0] == vertex_pair[0]:
                
                    vertex_pair_present = True

            if not vertex_pair_present:

                reformated_graph.append(vertex_pair)
    
    
    min_spanning_tree = []
    
    while len(min_spanning_tree) < (len(G) - 2) :
    
        min_index, temp_min_vertex_pair = min(enumerate(reformated_graph), key = lambda x: x[1][1])
            
        # check for cycles
        vertices_list = []

        vertices_list.append(temp_min_vertex_pair[0][0])
        vertices_list.append(temp_min_vertex_pair[0][1])

        for edge in min_spanning_tree:

            vertices_list.append(edge[0][0])
            vertices_list.append(edge[0][1])

        if len(set(vertices_list)) > len(vertices_list)/2:

            min_spanning_tree.append(temp_min_vertex_pair)

        reformated_graph.pop(min_index)

    # need to reformat for return output

    min_spanning_tree_dict = {}

    for entry in min_spanning_tree:

        if not entry[0][0] in min_spanning_tree_dict:

            min_spanning_tree_dict[entry[0][0]] = []

        if not entry[0][1] in min_spanning_tree_dict:
    
            min_spanning_tree_dict[entry[0][1]] = []

        min_spanning_tree_dict[entry[0][0]].append((entry[0][1],entry[1]))
        min_spanning_tree_dict[entry[0][1]].append((entry[0][0],entry[1]))

    return min_spanning_tree_dict



"""Question 4: Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like "question4(T, r, n1, n2)", where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4), and the answer would be 3."""

def question4(T, r, n1, n2):

    pass



"""Question 5: Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like "question5(ll, m)", where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position."""

def question5(ll, m):

    pass




