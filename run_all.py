import os

# List of scripts to run
scripts = [
    "shortest_path_analysis.py",
    "centrality_analysis.py",
    "temporal_centrality_analysis.py",
    "event_graph_generation.py",
    "multi_order_model.py"
]

# Execute each script
for script in scripts:
    print(f"Running {script}...")
    os.system(f"python3 {script}")
    print("Done.")
