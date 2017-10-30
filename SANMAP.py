#!/usr/bin/env python
# Author Dario Clavijo 2016
# GPLv3

import graphviz as gv
import functools

# creamos algunos estilos
styles = {
    'graph': {
        'label': 'FC SAN MAP',
        'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'hexagon',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor': '#006699',
    },
    'edges': {
        'style': 'dashed',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}

# funcion de ayuda para crear nodos
def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

# funcion de ayuda para cread conexiones
def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

# funcion de ayuda para aplicar estilos
def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )

    return graph


# funcion de ayuda para crear un enlace con label y color
def link(A,B,label,color):
	return ((A,B),
		{'label': label,
		 'style': 'dashed',
        	'color': color,
        	'arrowhead': 'open',
        	'fontname': 'Courier',
        	'fontsize': '12',
        	'fontcolor': 'white'
		})


# funcion de ayuda para crear un switch
def addsw(name):
 	return (name, {
        	'fontname': 'Helvetica',
        	'shape': 'hexagon',
        	'fontcolor': 'white',
        	'color': 'white',
        	'style': 'filled',
        	'fillcolor': '#006699',
    		})

# funcion de ayuda para crear un storage
def addstg(name):
 	return (name, {
        	'fontname': 'Helvetica',
        	'shape': 'cylinder',
        	'fontcolor': 'white',
        	'color': 'white',
        	'style': 'filled',
        	'fillcolor': '#660000',
		})

# funcion de ayuda para crear un host
def addhost(name):
 	return (name, {
        	'fontname': 'Helvetica',
        	'shape': 'square',
        	'fontcolor': 'white',
        	'color': 'white',
        	'style': 'filled',
        	'fillcolor': '#0000FF',
    		})

# arreglo de switches
switches = [
	addsw('switchcore1'),
	addsw('switchcore2'),
	addsw('switch1'),
	addsw('switch2'),
	]

# arreglo de storages
storages = [
	addstg('stg1'),
	addstg('stg2'),
	]

# arreglo de hosts
hosts = [
	addhost('VMWHOSTX'),
	]

# arreglo general
nodes = switches + storages + hosts

# arreglo de conexiones entre switches
switches = [
	link('switchcore1','switch1','isl','blue'),
	link('switchcore2','switch2','isl','blue'),
	link('switchcore1','switch1','isl','blue'),
	link('switchcore2','switch2','isl','blue')

	]

# arreglo de conexiones entre storages y switches
storages = [
	link('stg1','switchcore1','','red'),
	link('stg1','switchcore2','','red'),
	link('stg2','switchcore1','','red'),
	link('stg2','switchcore2','','red')
	]

# arreglo de conexiones entre hosts y switches
hosts = [
	link('VMWHOSTX','switch1','','white'),
	link('VMWHOSTX','switch2','','white')
	]

# arreglo general
links = switches + storages + hosts

def make_graph(nodes,edges,filename,format):
	# inicializamos la lib
	graph = functools.partial(gv.Graph, format=format)
	digraph = functools.partial(gv.Digraph, format=format)
	# parseo y renderizado del mapa
	g1 = add_edges(add_nodes(digraph(), nodes),edges)
	g1 = apply_styles(g1, styles)
	g1.render(filename)

# renderizamos en formato png y svg
make_graph(nodes,links,'img/fcsw','svg')
make_graph(nodes,links,'img/fcsw','png')
