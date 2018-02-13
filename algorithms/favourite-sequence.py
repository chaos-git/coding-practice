import sys
from Queue import PriorityQueue

class FavouriteSequence:
    def construct_dag(self, sequences):
        dag = {}  # key: value, value: (parents, children) tuple
        potential_roots = set()  # nodes without a parent
        for sequence in sequences:
            sequence_previous_node = None
            for element in sequence:
                if sequence_previous_node is None:
                    sequence_previous_node = element
                    dag[element] = dag.get(element, (set(), set()))
                    potential_roots.add(element)
                else:
                    (parent_parents, parent_children) = dag.get(sequence_previous_node, (set(), set()))
                    (child_parents, child_children) = dag.get(element, (set(), set()))
                    parent_children.add(element)
                    child_parents.add(sequence_previous_node)
                    dag[sequence_previous_node] = (parent_parents, parent_children)
                    dag[element] = (child_parents, child_children)
                sequence_previous_node = element
        return (dag, potential_roots)

    def calculate(self, sequences):
        (dag, potential_roots) = self.construct_dag(sequences)
        result = []
        queue = PriorityQueue()
        for potential_root in potential_roots:
            if not dag[potential_root][0]: # if no parents
                queue.put((potential_root))
        while not queue.empty():
            (element) = queue.get()
            result.append(element)
            for child in dag[element][1]:
                child_parents = dag[child][0]
                if element in child_parents:
                    child_parents.remove(element)
                if not child_parents:
                    queue.put((child))
            del dag[element]
        return result

sequences = [map(int, sequence.split()) for sequence in list(sys.stdin)[2::2]]
result = FavouriteSequence().calculate(sequences)
print " ".join(map(str, result))