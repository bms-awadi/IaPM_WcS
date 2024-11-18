import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Define tasks and durations for the Gantt Chart
gantt_data = {
    'Task': ['Data Collection', 'Algorithm Development', 'Testing', 'Deployment'],
    'Start': [0, 3, 7, 10],  # Start weeks
    'Duration': [3, 4, 3, 2],  # Duration in weeks
}

# Create a DataFrame for Gantt Chart
gantt_df = pd.DataFrame(gantt_data)

# Plotting the Gantt Chart
fig, ax = plt.subplots(figsize=(10, 5))
for index, row in gantt_df.iterrows():
    ax.barh(row['Task'], row['Duration'], left=row['Start'], color='lightblue')

ax.set_xlabel('Weeks')
ax.set_title('Gantt Chart for Recommendation Engine Project')
ax.invert_yaxis()
plt.savefig('gantt_chart.png')
plt.show()

# Define tasks with optimistic, most likely, and pessimistic estimates for PERT Chart
pert_data = {
    'Task': ['Data Collection', 'Algorithm Development', 'Testing', 'Deployment'],
    'Optimistic': [2, 3, 2, 1],
    'Most Likely': [3, 4, 3, 2],
    'Pessimistic': [5, 6, 4, 3],
}

# Create a DataFrame for PERT Chart
pert_df = pd.DataFrame(pert_data)

# Calculate Expected Time for each task
pert_df['Expected Time'] = (pert_df['Optimistic'] + 4 * pert_df['Most Likely'] + pert_df['Pessimistic']) / 6

# Create a directed graph for PERT Chart
G = nx.DiGraph()
G.add_edges_from([
    ('Start', 'Data Collection'),
    ('Data Collection', 'Algorithm Development'),
    ('Algorithm Development', 'Testing'),
    ('Testing', 'Deployment'),
    ('Deployment', 'End')
])

# Assign expected times as edge weights
weights = {
    ('Start', 'Data Collection'): pert_df.loc[0, 'Expected Time'],
    ('Data Collection', 'Algorithm Development'): pert_df.loc[1, 'Expected Time'],
    ('Algorithm Development', 'Testing'): pert_df.loc[2, 'Expected Time'],
    ('Testing', 'Deployment'): pert_df.loc[3, 'Expected Time'],
    ('Deployment', 'End'): 0 
}

nx.set_edge_attributes(G, weights, 'weight')

# Identify the critical path using the longest path in terms of duration
critical_path = nx.dag_longest_path(G, weight='weight')
critical_path_duration = nx.dag_longest_path_length(G, weight='weight')

# Plot the PERT Chart
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 5))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
for (u, v, d) in G.edges(data=True):
    x, y = pos[v]
    plt.text(x + 0.02, y, f"{d['weight']:.2f}", fontsize=8, ha='left', va='center', color='black')
plt.title('PERT Chart for Recommendation Engine Project')
plt.savefig('pert_chart.png') 

pert_df, critical_path, critical_path_duration
