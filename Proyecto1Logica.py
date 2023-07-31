import ply.lex as lex
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt

# Lista de tokens reconocidos por el lexer
tokens = ['VARIABLE', 'NOT', 'AND', 'OR', 'IMPLIES', 'IFF', 'LPAREN', 'RPAREN']

# Expresiones regulares para tokens
t_NOT = r'~'
t_AND = r'\^'
t_OR = r'o'
t_IMPLIES = r'=>'  # Implicación
t_IFF = r'<=>'    # Doble implicación
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Función para manejar el token VARIABLE
def t_VARIABLE(t):
    r'[pqrstuvwxyzb]'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para manejar errores de caracteres no reconocidos
def t_error(t):
    print(f"Carácter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Definición de las reglas gramaticales
def p_expression(p):
    '''expression : VARIABLE
                  | NOT expression
                  | expression AND expression
                  | expression OR expression
                  | expression IMPLIES expression
                  | expression IFF expression
                  | LPAREN expression RPAREN'''

    if len(p) == 2:
        # For a single variable, add it as a node to the graph
        if isinstance(p[1], str):
            G.add_node(p[1], label=p[1])  # Store the operator as the label
            p[0] = p[1]
        else:
            p[0] = ""
    elif len(p) == 3:
        # For NOT operator, add it as a node to the graph if it's not an empty node
        if p[1] + p[2]:  # Skip adding empty nodes
            operator = p[1]  # Get the operator
            G.add_node(p[1] + p[2], label=operator)  # Store the operator as the label
            G.add_edge(p[1] + p[2], p[2])  # Connect the operator node to its child
            p[0] = p[1] + p[2]
        else:
            p[0] = ""
    elif len(p) == 4:
        # For binary operators, add them as nodes and add edges to the graph if they are not empty nodes
        if p[1] + p[2] + p[3]:  # Skip adding empty nodes
            operator = p[2]  # Get the operator
            G.add_node(p[1] + p[2] + p[3], label=operator)  # Store the operator as the label
            G.add_edge(p[1] + p[2] + p[3], p[1])  # Connect the operator node to its left child
            G.add_edge(p[1] + p[2] + p[3], p[3])  # Connect the operator node to its right child
            p[0] = p[1] + p[2] + p[3]
        else:
            p[0] = ""

# Definición de precedencia y asociatividad de los operadores
precedence = (
    ('left', 'IFF'),
    ('left', 'IMPLIES'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
)

# Crear el parser
parser = yacc.yacc()

# Función para analizar una expresión y construir el grafo
def analizar_expresion(expresion):
    global G
    G = nx.DiGraph()  # Reset the graph before parsing a new expression
    parser.parse(expresion, lexer=lexer)
    return G

# Función para dibujar el grafo
def dibujar_grafo(G):
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')  # Get the labels from the 'label' attribute

    # Extract node labels and set the label to an empty string for nodes without labels
    node_labels = {node: labels.get(node, '') for node in G.nodes()}

    # Remove isolated nodes
    G.remove_nodes_from(list(nx.isolates(G)))

    nx.draw(
        G,
        pos,
        with_labels=True,
        labels=node_labels,
        node_size=2000,
        node_color="blue",
        font_size=10,
        font_weight='bold',
        arrowsize=20,
        font_color='black',
        edge_color='gray',
        width=1.5,
        alpha=0.8,
    )
    plt.show()  # Show the graph without creating an extra figure

# Ejemplo de uso
expresion_logica = '~~~q'
grafo = analizar_expresion(expresion_logica)
dibujar_grafo(grafo)
