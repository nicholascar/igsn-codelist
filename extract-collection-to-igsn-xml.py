import rdflib

g = rdflib.Graph()
g.load('skos.ttl', format="turtle")
q = '''
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>  
    SELECT (COUNT(?s) AS ?cnt) 
    WHERE { 
        ?s skos:definition ?o . 
        FILTER(STRLEN(?o) <= 0)
    }'''
for r in g.query(q):
    print(r)
