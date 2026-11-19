

from collections import deque
from network_support import validate_request, record_step
from app_runner import run
STAGE = 3  # Monday 1; Tuesday 2 when traversals work; Thursday 3 when routes work.
MY_RESTRICTION = "A"  # Set this to your instructor-issued case in your personal copy.


# MONDAY — Inspect the supplied model and test copies with a connection mistake.
# No traversal is required for STAGE 1; keep your brief personal model notes.


# TUESDAY — Complete each algorithm separately on the fresh common fixture.
def breadth_first(graph, start):
    validate_request(graph, start)
    queue = deque([start])
    discovered = {start}
    order = []
    trace = []
    edge_examined = 0
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            edge_examined += 1
            if neighbor not in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)
        record_step(trace, node, queue, discovered)
    """Return BFS order, independent snapshots, and adjacency entries examined."""
    return order, trace, edge_examined
    # validate_request(graph, start)
    # Begin a deque with start and a discovered set containing start.
    # Use separate order, trace, and edge-count state.
    # Process the queue from the left and append each new visit to order.
    # Examine neighbors in their listed order, counting each adjacency entry.
    # Mark an undiscovered neighbor before adding it to the queue.
    # Use record_step(trace, node, queue, discovered) after neighbor handling.
    # Return order, trace, and the count; leave graph unchanged.
    # raise NotImplementedError("Complete breadth-first traversal.")


def depth_first(graph, start):
    validate_request(graph, start)
    stack = [start]
    visited = set()
    order = []
    trace = []
    edge_examined = 0
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph[node]):
            edge_examined += 1
            if neighbor not in visited:
                stack.append(neighbor)
        record_step(trace, node, stack, visited)
    
    return order, trace, edge_examined
    
    # """Return iterative DFS order, independent snapshots, and adjacency count."""
    # validate_request(graph, start)
    # Begin a list stack with start and an empty visited set.
    # Pop from the right; skip an entry already processed.
    # Mark this new visit and record its order.
    # Consider reversed neighbors so the first listed neighbor is taken next.
    # Count each adjacency entry and push neighbors not yet visited.
    # Use record_step(trace, node, stack, visited) after neighbor handling.
    # Return order, trace, and the count; leave graph unchanged.
    # raise NotImplementedError("Complete iterative depth-first traversal.")


# THURSDAY — Save parents during BFS, then follow one chain backward.
def reconstruct_path(parents, goal):
    """Return start-to-goal order by following the BFS parent chain."""
    path = []
    current = goal
    
    while current is not None:
        path.append(current)
        current = parents[current]
        
        
    path.reverse()
    return path


def shortest_hop_path(graph, start, goal, blocked=()):
    """Return a permitted fewest-hop path and parents, or None with parent state."""
    blocked_nodes = set(blocked)
    validate_request(graph, start, goal, blocked_nodes)
    if start in blocked_nodes or goal in blocked_nodes:
        return None, {}
    
    parents = {start: None}
    if start == goal:
        return [start], parents
    
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            return reconstruct_path(parents, goal), parents
        for neighbor in graph[node]:
            if neighbor not in parents and neighbor not in blocked_nodes:
                parents[neighbor] = node
                queue.append(neighbor)
    return None, parents


def main():
    """Run only the selected completed stage using supplied presentation."""
    run(STAGE, breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION)


if __name__ == "__main__":
    main()
