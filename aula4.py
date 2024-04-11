import json
from graphviz import Digraph

automato : dict = {}

with open ('automato.json', "r", encoding="utf-8") as f:
    automato = json.load(f)

    dot = Digraph(comment='Automato')

    # criar um nó inicial
    dot.node('start', shape='none', label='')

    # criar uma transição inicial
    dot.edge('start', automato['q0'], label='')

    for state in automato["delta"].keys():

        if state in automato["F"]:
            dot.node(state, state, shape='doublecircle')

        else:
            dot.node(state, state, shape='circle')

    for estado_inicial, transition in automato["delta"].items():
        for simbolo, estado_final in transition.items():
            dot.edge(estado_inicial, estado_final, label=simbolo)
    
    dot.render('automato_grafo', format='png', view=True)

    