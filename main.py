import graphviz

# Ejemplo simple de grafo dirigido con graphviz
g = graphviz.Digraph("G", filename="ejemplo_grafo", format="png")
g.attr(rankdir="LR", size="8,5")
g.attr("node", shape="circle", style="filled", color="lightblue")

g.node("A", "Inicio")
g.node("B", "Proceso")
g.node("C", "Decisión")
g.node("D", "Fin")

g.edge("A", "B", label="sigue")
g.edge("B", "C", label="evalúa")
g.edge("C", "B", label="no")
g.edge("C", "D", label="sí")

# Mostrar la definición DOT y renderizar a PNG en el directorio actual
print(g.source)
output_path = g.render(cleanup=True)
print(f"Grafo renderizado en: {output_path}")
