import networkx as nx
import csv
import os


def rwr(network_file, weights_file, outfile):
    pass


if __name__ == "__main__":
    rwrd = "."
    network_file = os.path.join(rwrd, "data/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv")
    weights_file = os.path.join(rwrd, "data/tAML_P3_SNV_polyphen_15390_nodes.tsv")
    outfile = os.path.join(rwrd, "output/RW_tAML_P3_nx.tsv")

    # a comment
    rwr(network_file, weights_file, outfile)
