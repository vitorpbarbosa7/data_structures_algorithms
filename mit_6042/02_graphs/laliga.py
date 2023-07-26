import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
G = nx.DiGraph()

# Define the teams
teams = ['Barcelona', 'Real Madrid', 'Atletico Madrid', 'Sevilla', 'Valencia', 'Real Sociedad', 'Getafe', 'Villarreal', 'Granada', 'Athletic Bilbao']

# Add the teams as nodes to the graph
G.add_nodes_from(teams)

# Define the matches and their outcomes
matches = [
    ('Barcelona', 'Real Madrid', 'Barcelona'),   # Barcelona won against Real Madrid
    ('Real Madrid', 'Barcelona', 'Draw'),        # Real Madrid drew against Barcelona
    # Add more matches here
]

# Add the directed edges to the graph representing the matches
for match in matches:
    home_team, away_team, outcome = match
    if outcome == 'Barcelona':
        G.add_edge(home_team, away_team)
    elif outcome == 'Real Madrid':
        G.add_edge(away_team, home_team)
    # Add more conditions for different outcomes

# Draw the directed graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_weight='bold')
plt.title("La Liga Games 2020")
plt.show()

