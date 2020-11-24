import sys
from graph import Graph, Vertex


def create_graph(filename):
    """
    Reads file and creates a grid from the first line of text
    Rows then columns. Assigns prisoner and exit vertex.

    :param filename: File being parsed
    :return: returns graph, prisoner vertex, and vertex exit
    """

    prison_graph = Graph()
    prisoner_vertex = None
    exit_vertex = None
    vertices = {}
    cameras = set()

    with open(filename, 'r') as graph_file:
        row, col = map(int, graph_file.readline().split())
        print(f'Graph Size... Rows: {row} Columns: {col}')
        for line in graph_file:
            line = line.strip()
            cam_x, cam_y = map(int, line.split())
            cameras.add((cam_x, cam_y))
            print(f'Camera at: {cam_x},{cam_y}')

    for i in range(row):  # iterate over rows
        for j in range(col):  # iterate over columns
            vert = Vertex(f'{i},{j}')
            vertices[(i, j)] = vert

            if vert in cameras:
                vert.has_camera = True

            prison_graph.add_vertex(vert)

    # determine if there is a bordering cell without a camera and create
    # an undirected edge
    for i in range(row):
        for j in range(col):
            source_vertex = vertices[(i, j)]
            # if nothing up & no camera
            destination_vertex = (i - 1, j)
            if destination_vertex in vertices:
                prison_graph.add_undirected_edge(source_vertex,
                                                 destination_vertex)
            # if nothing down & no camera
            # if nothing right & no camera
            # if nothing left & no camera

    for x in vertices:
        print(x, getattr(vertices[x], 'label'))

    # for key, values in prison_graph.adjacency_list.items():
    #     print(f'{getattr(key, "label")} : {values}')

    # The following line is here as a placeholder. Replace
    # this line with the real return values once you
    # load them from the prison data file.
    return prison_graph, prisoner_vertex, exit_vertex


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
