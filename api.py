# Importa las bibliotecas necesarias para trabajar con grafos, interfaces de usuario personalizadas y gráficos.
import networkx as nx
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 

# Crea un grafo vacío usando NetworkX.
G = nx.Graph()

# Crea la ventana principal de la aplicación usando CustomTkinter.
root = ctk.CTk()
root.title("Algoritmo de busqueda en Anchura")  # Establece el título de la ventana.

# Configura la ventana principal para que se ajuste automáticamente al tamaño de sus contenidos.
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Crea un marco principal dentro de la ventana para contener otros widgets.
main_frame = ctk.CTkFrame(root)
main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Añade el marco a la ventana y lo ajusta.

# Configura el marco principal para que se ajuste automáticamente al tamaño de sus contenidos.
for i in range(6):  
    main_frame.grid_rowconfigure(i, weight=1)
for j in range(2):  
    main_frame.grid_columnconfigure(j, weight=1)

# Crea y posiciona los widgets para la entrada de vértices y aristas.
vertex_label = ctk.CTkLabel(main_frame, text="Vertice:")
vertex_label.grid(row=0, column=0, columnspan=2, pady=(0, 5), sticky="ew")  

vertex_entry = ctk.CTkEntry(main_frame)
vertex_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")  

add_vertex_button = ctk.CTkButton(main_frame, text="Agregar vertice", command=lambda: G.add_node(vertex_entry.get()))
add_vertex_button.grid(row=2, column=0, columnspan=2, sticky="ew")  

edge_label_1 = ctk.CTkLabel(main_frame, text="Arista inicio:")
edge_label_1.grid(row=3, column=0, pady=(0, 0), sticky="ew")  

edge_entry_1 = ctk.CTkEntry(main_frame)
edge_entry_1.grid(row=4, column=0, pady=(0, 0), sticky="ew")  

edge_label_2 = ctk.CTkLabel(main_frame, text="Arista fin:")
edge_label_2.grid(row=3, column=1, pady=(0, 0), sticky="ew")  

edge_entry_2 = ctk.CTkEntry(main_frame)
edge_entry_2.grid(row=4, column=1, pady=(0, 0), sticky="ew")  

add_edge_button = ctk.CTkButton(main_frame, text="Agregar arista", command=lambda: G.add_edge(edge_entry_1.get(), edge_entry_2.get()))
add_edge_button.grid(row=5, column=0, columnspan=2, sticky="ew")  

print_info_button = ctk.CTkButton(main_frame, text="Info de datos agregados (consola)", command=lambda: print("Numero de nodos:", G.number_of_nodes(), "\nNumero de bordes:", G.number_of_edges()))
print_info_button.grid(row=6, column=0, columnspan=2, pady=(0,5), sticky="ew")  

# Define las funciones para dibujar el grafo y realizar la búsqueda en anchura.
def draw_graph(G, ax, highlight=None):
    ax.clear()  # Limpia el subplot antes de dibujar
    pos = nx.spring_layout(G)  # Calcula la posición de los nodos
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue')
    if highlight:  # Si se proporciona una lista de nodos/aristas para resaltar
        # Asegúrate de que highlight contenga aristas y no nodos
        highlight_nodes = [edge[0] for edge in highlight] + [edge[1] for edge in highlight]
        highlight_edges = highlight
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='red', ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', ax=ax)

def show_bfs():
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    source_node = vertex_entry.get().strip()  # Asegúrate de eliminar espacios en blanco
    print(f"Intentando buscar desde el nodo fuente: '{source_node}'")  # Diagnóstico
    if source_node not in G:
        print("El nodo fuente no existe en el grafo.")
        return
    # El resto de tu código sigue aquí
    bfs_edges = list(nx.bfs_edges(G, source=source_node))
    bfs_tree = nx.Graph()
    bfs_tree.add_edges_from(bfs_edges)  # Crea un nuevo grafo solo con las aristas de BFS

    draw_graph(G, axs[0])  # Dibuja el grafo original en el primer subplot
    draw_graph(bfs_tree, axs[1], highlight=bfs_edges)  # Dibuja el grafo de BFS en el segundo subplot, resaltando las aristas de BFS

    # Muestra la figura en el canvas de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=main_frame)  # Asume que main_frame es tu marco principal
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=2, rowspan=6, padx=(10, 0), sticky="nsew")
    canvas.draw()

def show_dfs():
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    source_node = vertex_entry.get().strip()  # Obtiene el nodo fuente de la entrada del usuario
    if source_node not in G:
        print("El nodo fuente no existe en el grafo.")
        return

    # Realiza la búsqueda en profundidad (DFS) desde el nodo fuente
    dfs_edges = list(nx.dfs_edges(G, source=source_node))
    dfs_tree = nx.Graph()
    dfs_tree.add_edges_from(dfs_edges)  # Crea un nuevo grafo solo con las aristas de DFS

    # Dibuja el grafo original y el grafo de DFS en dos subplots
    draw_graph(G, axs[0])  # Dibuja el grafo original en el primer subplot
    draw_graph(dfs_tree, axs[1], highlight=dfs_edges)  # Dibuja el grafo de DFS en el segundo subplot, resaltando las aristas de DFS

    # Muestra la figura en el canvas de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=main_frame)  # Asume que main_frame es tu marco principal
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=1, column=2, rowspan=6, padx=(10, 0), sticky="nsew")
    canvas.draw()

# Ahora que show_bfs está definida, crea los botones que la utilizan.
draw_button = ctk.CTkButton(main_frame, text="Dibujar grafo", command=show_bfs)
draw_button.grid(row=7, column=0, padx=(0,5), sticky="ew")  

bfs_button = ctk.CTkButton(main_frame, text="Busqueda en anchura", command=lambda: show_bfs())
bfs_button.grid(row=7, column=1, padx=(5,0), sticky="ew")

dfs_button = ctk.CTkButton(main_frame, text="Búsqueda en profundidad", command=show_dfs)
dfs_button.grid(row=8, column=0, columnspan=2, sticky="ew", pady=(5,0))

# Configura Matplotlib para la visualización del grafo.
figure = Figure(figsize=(5, 5))
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=6, padx=(10, 0), sticky="nsew")

# Configura la ventana principal para ajustarse automáticamente al tamaño de sus contenidos.
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Inicia el bucle principal de la aplicación Tkinter.
root.mainloop()