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
    print(f'lines len: {len(lines)}, lines: {lines}')

    prisoner_vertex = Graph()
    prisoner_vertex.add_vertex('0, 0')  # prisoner always starts at 0, 0
    print(f'Prisoner starting location: {prisoner_vertex.adjacency_list}\n')

    for i, line in enumerate(lines):
        print(f'Line {i}: {line.strip()} and type is "{line.__class__}"')
        if i == 0:  # finds first line, determines size of the graph
            # prison_graph = [int(line[0:1]), int(line[2:3])]
            prison_graph = Graph()
            prison_graph.add_vertex(f'{line[0:1]},{line[2:3]}')
            print(f'Graph size {prison_graph.adjacency_list}')

            exit_vertex = Vertex('exit', False)
            exit_vertex.add_vertex(f'{int(line[0:1]) - 1},'
                                   f'{int(line[2:3]) - 1}')
            print(f'exit vertex {exit_vertex.adjacency_list}\n')

        else:  # the rest of the lines are coordinates of the cameras
            cameras.append(f'{int(line[0:1])},{int(line[:-2])}')
            print(f'adding line {i} to the camera list')
            print(f'cameras: {cameras}\n')
            # print(f'Camera #{i - 1} is located at ({cameras[i]})')

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
