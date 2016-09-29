class Tree_Node(object):
    """
    A Tree_Node, it holds data and a list of children node, it can add and search for nodes.
    """
    def __init__(self, data=None, children=None, is_last_node=False):
        self.data = data
        self.children = []
        self.is_last_node = False #Determines if last node in the tree

    def add_child(self, new_child): #Adds a new node as a child to a given node.
        self.children.append(new_child)

    def get_child(self, data): #Searches the children of a given node for a child with a particular value
        for child in self.children:
            if child.data == data:
                return child
        return None

WILDCARD = '*'
COMMA = ','
SLASH = '/'

def build_tree():
    """
    Builds a tree with all the parts of given patterns from stdin. This algorithm inserts
    parts of ever pattern one by one, if a part already exist along the current node's children
    it traverses until forced to make a new node with a part that isn't already in the tree.
    """
    Tree_Head = Tree_Node(data='head')
    num_of_patterns = int(input().strip())

    for num in range(num_of_patterns):
        pattern_parts = input().strip().split(COMMA)
        current = Tree_Head
        for i in range(len(pattern_parts)):
            part = pattern_parts[i]
            child = current.get_child(part)
            if child: current = child
            else:
                new_node = Tree_Node(data=part)
                current.add_child(new_node)
                current = new_node
            if i == (len(pattern_parts)-1): current.is_last_node = True
    return Tree_Head

def traverse_tree(head, path_list, current_pattern):
    """
    Traverses a pattern tree and returns a list of all possible patterns. Each part of the pattern
    is checked among the current node's children for either the part or a wild card. If either
    are found, it recursively traverses to that/those nodes and moves to the next part of the path.
    Once the end of the path has been reached the current pattern is returned within a list.
    """
    if not path_list and head.is_last_node:# If end reached, remove trailing comma and return pattern
        return [current_pattern[:-1]]
    elif not path_list:
        return []

    value = path_list[0]
    path_list = path_list[1:]
    matched_patterns = []
    found_child = head.get_child(value)
    if found_child:
        exact_match = traverse_tree(found_child,path_list,current_pattern+value+COMMA)
        matched_patterns = exact_match

    wild_child = head.get_child(WILDCARD)
    if wild_child:
        wild_return = traverse_tree(wild_child,path_list,current_pattern+WILDCARD+COMMA)
        matched_patterns = matched_patterns + wild_return
    return matched_patterns

def get_correct_paterns(pattern_list):
    """
    Returns patterns, with the least number of wildcards.
    """
    least_list = []
    least = None

    for pattern in pattern_list:
        wild_count = pattern.count(WILDCARD)

        if least == None: #if fisrt iteration, assign least
            least = wild_count

        if wild_count < least:
            least = wild_count
            least_list[:] = []
            least_list.append(pattern)
        elif wild_count == least: least_list.append(pattern)

    if len(least_list) > 1: return reduce(least_list)
    else: return least_list

def reduce(pattern_fields):
    """
    Return the pattern whose wildcards are furthest to the right.
    """
    reduced_pattern = None
    highest = None

    for pattern in pattern_fields:
        wild_count = sum([i for i, j in enumerate(pattern) if j == WILDCARD])

        if highest is None: #if first iteration, assign highest
            highest = wild_count
            reduced_pattern = pattern
        elif wild_count > highest:
            highest = wild_count
            reduced_pattern = pattern
    return [reduced_pattern]

def main():
    """
    This program reads patterns and paths from stdin. From the given patterns a tree
    is constructed with each node containing the parts of each pattern. Using each part
    of a given path, this program traverses the pattern tree until the appropriate pattern
    is found. If mulitiple patterns are found, it then reduces the options until one pattern
    remains for a given path, if no pattern is found "NO MATCH" is printed.
    """
    Tree_Head = build_tree() #builds a tree with patterns given from stdin, returns head of the tree
    num_paths = int(input())
    for num in range(num_paths):
        path = input().strip()
        path = [part for part in path.split(SLASH) if part != ''] #covert path to list parts separated by "/", excluding parts = ""
        patterns = get_correct_paterns(traverse_tree(Tree_Head, path, ''))
        if patterns:
            print(patterns[0])
        else:
            print('NO MATCH')

if __name__ == '__main__':
    main()
