# Importa las bibliotecas necesarias para trabajar con grafos, interfaces de usuario personalizadas y gráficos.
import networkx as nx
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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

draw_button = ctk.CTkButton(main_frame, text="Dibujar grafo", command=lambda: draw_graph())
draw_button.grid(row=7, column=0, padx=(0,5), sticky="ew")  

bfs_button = ctk.CTkButton(main_frame, text="Busqueda en anchura", command=lambda: show_bfs())
bfs_button.grid(row=7, column=1, padx=(5,0), sticky="ew")  

# Configura Matplotlib para la visualización del grafo.
figure = Figure(figsize=(5, 5))
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=1, column=2, rowspan=6, padx=(10, 0), sticky="nsew")

# Configura la ventana principal para ajustarse automáticamente al tamaño de sus contenidos.
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Define las funciones para dibujar el grafo y realizar la búsqueda en anchura.
def draw_graph(bfs_edges=None):
    ax.clear()
    if bfs_edges:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=ax, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=bfs_edges, edge_color='r', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[vertex_entry.get()]+[v for u, v in bfs_edges], node_color='r', ax=ax)
    else:
        nx.draw(G, ax=ax, with_labels=True)
    canvas.draw()

def show_bfs():
    bfs_edges = list(nx.bfs_edges(G, source=vertex_entry.get()))
    draw_graph(bfs_edges)
    canvas.draw()

def hola_mundo():
    print("hola mundo")

# Inicia el bucle principal de la aplicación Tkinter.
root.mainloop()