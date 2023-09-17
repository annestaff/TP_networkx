import networkx as nx
import csv
import os


def rwr(network_file, weights_file, outfile):
    g = nx.Graph()

    with open(network_file, "r") as f:
        csv_reader = csv.reader(f,delimiter="\t")
        for row in csv_reader:
            g.add_edge(row[0], row[1])

    weight_dict = {}

    with open(weights_file, "r") as f:
        csv_reader = csv.reader(f, delimiter="\t")
        for name, weight in csv_reader:
            weight_dict[name] = float(weight)

    pagerank_results = nx.pagerank(g, personalization=weight_dict, alpha=0.9)

    with open(outfile, "w") as f:
        for node,rank in pagerank_results.items():
            print(f"{node}\t{rank:.9f}", file=f)


if __name__ == "__main__":
    rwrd = "."
    network_file = os.path.join(rwrd, "data\\PPI_HiUnion_LitBM_APID_gene_names_190123.tsv")
    weights_file = os.path.join(rwrd, "data\\tAML_P3_SNV_polyphen_15390_nodes.tsv")
    outfile = os.path.join(rwrd, "output\\RW_tAML_P3_nx.tsv")

    rwr(network_file, weights_file, outfile)
