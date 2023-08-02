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
t_IMPLIES = r'=>'
t_IFF = r'<=>'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_VARIABLE(t):
    r'[0123456789pqrstuvwxyzb]'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

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
    global counter

    if len(p) == 2:  # if the length of p is 2, then we are looking at a variable or a negation
        if isinstance(p[1], str):  # if it is a variable
            node_id = f'{p[1]}_{counter}'
            G.add_node(node_id, label=p[1])
            counter += 1
            p[0] = node_id
        else:  # if it is a negation
            p[0] = p[1]
    elif len(p) == 3:  # we are looking at a negation
        node_id = f'{p[1]}_{counter}'
        G.add_node(node_id, label=p[1])
        counter += 1
        G.add_edge(node_id, p[2])
        p[0] = node_id
    elif len(p) == 4:  # we are looking at a binary operator
        if p[1] == '(' and p[3] == ')':  # Handle expressions like (p AND q) directly
            p[0] = p[2]
        else:
            operator = p[2]
            if operator in G.nodes():  # if the operator has already been used before, reuse the node
                node_id = operator
            else:
                node_id = f'{operator}_{counter}'
                G.add_node(node_id, label=operator)
                counter += 1
            G.add_edge(node_id, p[1])
            G.add_edge(node_id, p[3])
            p[0] = node_id
    else:  # we are looking at something enclosed by parentheses
        p[0] = p[2]


precedence = (
    ('right', 'NOT'),
    ('left', 'IMPLIES', 'IFF'),
    ('left', 'AND', 'OR'),
)

def yacc_reset():
    global G, counter
    G = nx.DiGraph()
    counter = 0

parser = yacc.yacc()

def analizar_expresion(expresion):
    yacc_reset()
    parser.parse(expresion, lexer=lexer)
    return G, counter - 1  # Devolvemos el grafo y el índice del último nodo creado

def dibujar_grafo(G):
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    labels = nx.get_node_attributes(G, 'label')
    node_labels = {node: labels.get(node, '') for node in G.nodes()}
    
    # Filtramos los nodos que son paréntesis antes de dibujar el grafo
    nodes_to_draw = [node for node in G.nodes() if node in labels]
    
    G_filtered = G.subgraph(nodes_to_draw)  # Creamos un subgrafo con los nodos que se van a dibujar

    nx.draw(
        G_filtered,
        pos,
        with_labels=True,
        labels=node_labels,
        node_size=2000,
        node_color="lightblue",
        font_size=10,
        font_weight='bold',
        arrowsize=20,
        font_color='black',
        edge_color='gray',
        width=1.5,
        alpha=0.8,
    )
    plt.show()

expresion_logica = '(~(p^(qor))os)'
grafo, _ = analizar_expresion(expresion_logica)
dibujar_grafo(grafo)