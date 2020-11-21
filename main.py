import sys
from graph import Graph, Vertex


def create_graph(filename):
    # TO-DO: read the lines in the specified file
    # to create a Graph object. Returns 3 values:
    #
    #     prison_graph, prisoner_vertex, exit_vertex

    prison_file = open(filename, 'r')
    lines = prison_file.readlines()
    cameras = []
    prison_graph = Graph()

    yx_value = lines[0].strip()
    print(f'yx_value : {yx_value}, rows={yx_value[0]} , columns'
          f'={yx_value[-1]}')

    # construct the graph object by taking in the first line of lines
    # and iterate through defining vertices
    for i in range(0, int(yx_value[-1])):  # iterates rows
        for j in range(0, int(yx_value[0])):  # iterates columns
            prison_graph.add_vertex(Vertex(f'{i},{j}', False))
            print(getattr(Vertex(f'{j},{i}'), 'label'), end=' ')
            print(getattr(Vertex(f'{j},{i}'), 'visited'))

    for x in prison_graph.adjacency_list:
        print(getattr(x, 'label'))

    # for x in getattr(prison_graph, 'adjacency_list'):
    #     print(getattr(Vertex(prison_graph.adjacency_list[x]), 'label'))



    # The following line is here as a placeholder. Replace
    # this line with the real return values once you
    # load them from the prison data file.
    return None, None, None


def count_exit_paths(g, start_vertex, exit_vertex):
    # TO-DO: use depth-first-search to count how many distinct
    # paths exist from the given start vertex to the given
    # exit vertex. May be used recursively, if desired.

    # The following line is here as a placeholder. Replace
    # this line with the real return value once you determine
    # the correct result.
    return 0


# create_graph('/Prison_3x4.txt')

if __name__ == "__main__":
    # prison_filename = sys.argv[1]
    prison_filename = 'venv/Prison_3x4.txt'
    create_graph(prison_filename)
    # prison_graph, prisoner_vertex, exit_vertex = create_graph(prison_filename)
    # num_paths = count_exit_paths(prison_graph, prisoner_vertex, exit_vertex)
    # print(num_paths)
