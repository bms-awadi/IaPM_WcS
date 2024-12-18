def print_multiplication_table(n):
    print(f"Table de multiplication de {n} :")
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")
    print()  # Ligne vide pour séparer les tables

def main():
    print("Tables de multiplication de 1 à 10")
    print("==================================")
    
    for number in range(1, 11):
        print_multiplication_table(number)

if __name__ == "__main__":
    main()

exit(0)

from matplotlib import pyplot as plt
import networkx as nx

G = nx.DiGraph()

# Add nodes
G.add_node("Clients", shape="rectangle")
G.add_node("Comptes", shape="rectangle")
G.add_node("Client_Compte", shape="rectangle")
G.add_node("Transactions", shape="rectangle")

# Add edges with relationships
G.add_edge("Clients", "Client_Compte", label="1,n")
G.add_edge("Client_Compte", "Comptes", label="n,1")
G.add_edge("Comptes", "Transactions", label="1,n")

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold"
)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={("Clients", "Client_Compte"): "1,n",
                         ("Client_Compte", "Comptes"): "n,1",
                         ("Comptes", "Transactions"): "1,n"},
    font_color="red",
)

plt.title("Schéma des relations pour la base de données bancaire", fontsize=12)
plt.show()
