import logging
import os, codecs

from argparse import ArgumentParser
from pathlib import Path

from pyrml.pyrml_mapper import RMLConverter
from pyrml.functions import *

from rdflib import Graph

parser = ArgumentParser()
parser.add_argument("-o", "--output", dest="output",
            help="Output file. If no choice is provided then standard output is assumed as default.", metavar="RDF out file")
parser.add_argument("-m", action="store_true", default=False,
            help="Enable conversion based on multiproccessing for fastening the computation.")
parser.add_argument("input", help="The input RML mapping file for enabling RDF conversion.")
parser.add_argument("ontology", help="The main ontology to create the generated KG.")
        
args = parser.parse_args()
logging.basicConfig(level=logging.DEBUG)
    
def execute_mapping():
    rml_converter = RMLConverter.get_instance()
    g = rml_converter.convert(args.input) 
    return g

def store(g, output):    
    dest_folder = Path(output).parent
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        
    with codecs.open(output + '.ttl', 'w', encoding='utf8') as out_file:
        out_file.write(g.serialize(format='turtle'))

    with codecs.open(output + '.n3', 'w', encoding='utf8') as out_file:
        out_file.write(g.serialize(format='nt'))

if __name__ == '__main__':
    g = execute_mapping()
    store(g, args.output)

    og = Graph()
    og.parse(args.ontology)
    og = og + g
    store(og, args.output + '_merged')
