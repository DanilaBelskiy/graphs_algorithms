class Node:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.path = []
        self.close_status = False
        self.connections = {}

    def change_weight(self, new_weight, johnson_flag: bool = False):
        if not johnson_flag:
            if new_weight < self.weight:
                self.weight = new_weight
        else:
            self.weight = new_weight

    def add_connection(self, node_name, weight):
        self.connections[node_name] = weight

    def change_connection(self, node_to, new_weight):
        self.connections[node_to] = new_weight

    def delete_connection(self, node_name):
        for i in self.connections.keys():
            if i.name == node_name:
                del self.connections[i]
                break

    def sort_connections(self):
        self.connections = dict(sorted(self.connections.items(), key=lambda item: item[0].weight))

    def amount_of_connections(self):
        return len(self.connections)

    def set_path(self, new_path: list):
        self.path = new_path

    def is_closed(self):
        return self.close_status

    def close(self):
        self.close_status = True

    def print_node(self):
        print(f'Name: {self.name}\nWeight: {self.weight}\nIs closed: {self.close_status}\nConnections:')
        for i in self.connections.keys():
            print(f"{i.name} ({i.weight}) = {self.connections[i]}")
        print("\n")
