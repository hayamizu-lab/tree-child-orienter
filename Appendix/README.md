# A program used to generate the input data for the experiments

This section describes how to use the random binary graphs program that produces the input data used in the experiments in the paper.  
The project is written in Python and can be run in the Python environment.

## Environment set-up

First, clone this repository to your local machine and access the main directory using the command below:
```terminal
git clone https://github.com/hayamizu-lab/tree-child-orienter.git
cd tree-child-orienter
```

## Prerequisites
To run this project, you may require the following packages:
+ sys
+ numpy
+ networkx
+ matplotlib
+ networkx
+ csv
+ itertools
+ random

## How to use
To run the program to generate random binary graphs, use:
```
python generate-binary-graphs.py
```
When you run the code, you will be prompted for the name of the output file and the values of the following parameters: `n` (the number of leaves), `r` (probability of occurrence of reticulation) and `k` (the number of networks to be generated).
```
Filename n r k: sample-network 10 0.1 100
```

According to the parameters, the program outputs k undirected networks with n leaves. The adjacency matrix of each network is saved as a CSV file and a visualisation is saved as a PDF file.  
[sample-network.pdf](sample-network.pdf)

### Notes
+ If you want to change the location of the output files, add an absolute or relative path as shown below.  
```python
plt.savefig('/path/to/your/output/directory/' + filename + '.pdf', format='pdf')
```
```python
np.savetxt('/path/to/your/output/directory/' + filename + '.csv', adjacency_matrix, delimiter=",", fmt="%d")
