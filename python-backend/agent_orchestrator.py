# agent_orchestrator.py - Koray Agent Flow Orchestrator v2.3
# Usage: python agent_orchestrator.py --workflow "research-map-brief" --output_graph "agent_flow.gexf"

import argparse
import networkx as nx

def orchestrate_agents(workflow):
    """Build and run agent flow graph using NetworkX."""
    G = nx.DiGraph()
    # Example workflow: research → map → brief
    edges = [("koray-researcher-agent", "koray-mapper-agent"), ("koray-mapper-agent", "koray-brief-generator-agent")]
    G.add_edges_from(edges)
    # Add attributes (e.g., tasks)
    for node in G.nodes:
        G.nodes[node]["task"] = "Execute " + node
    # Run topological sort for execution order
    order = list(nx.topological_sort(G))
    return G, order

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Orchestrate Koray agents as graph")
    parser.add_argument("--workflow", type=str, required=True, help="Comma-separated workflow e.g. research,map,brief")
    parser.add_argument("--output_graph", type=str, default="agent_flow.gexf")
    args = parser.parse_args()
    
    G, order = orchestrate_agents(args.workflow.split(","))
    nx.write_gexf(G, args.output_graph)
    print(f"Agent flow graph saved to {args.output_graph}")
    print("Execution Order:", order)