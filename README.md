# Tree-Child Orienter: Algorithms for Orienting Undirected Binary Phylogenetic Networks to a Desired Class

This repository contains the implementation of algorithms to determine whether a given undirected binary phylogenetic network can be oriented to a directed phylogenetic network of a desired class C, in particular, the class of tree-child networks, and to find a tree-child orientation of the graph if one exists. The main focus is on our practical exponential algorithm for solving the C-Orientation problem, adapted to the tree-child orientation problem as `TC-orientation` (Algorithm 1 in our paper). We have implemented this algorithm along with an existing exact exponential-time algorithm for C-Orientation, `TC-orientation-bruteforce` ([Algorithm 2 in Huber et al 2024](https://doi.org/10.1016/j.jcss.2023.103480)), and a heuristic method we developed specifically for the tree-child orientation problem, `TC-orientation-heuristic` (Algorithm 2 in our paper). We conducted performance comparison experiments to evaluate the accuracy and computation time of these algorithms. The repository also contains a program to generate undirected binary phylogenetic networks for the experiments. 

This repository serves as the supporting material for the paper:

> Tsuyoshi Urata, Manato Yokoyama, and Momoko Hayamizu. **Orientability of Undirected Phylogenetic Networks to a Desired Class: Practical Algorithms and Application to Tree-Child Orientation**. In _24th International Workshop on Algorithms in Bioinformatics (WABI 2024)_. Leibniz International Proceedings in Informatics (LIPIcs), Volume 312, pp. 9:1-9:17, Schloss Dagstuhl – Leibniz-Zentrum für Informatik (2024) https://doi.org/10.4230/LIPIcs.WABI.2024.9

## Repository Structure

The repository is organized as follows:

* `code`: Contains all the code used for the experiments in our paper
  * `TC-orientation`: Implementation of our practical exponential algorithm for C-Orientation, adapted to the Tree-Child Orientation problem (Algorithm 1)
  * `TC-orientation-bruteforce-huber2024`: Implementation of the existing exact exponential-time algorithm for C-Orientation  ([Algorithm 2 in Huber et al 2024](https://doi.org/10.1016/j.jcss.2023.103480))
  * `TC-orientation-heuristic`: Implementation of our heuristic method specifically developed for the tree-child orientation problem (Algorithm 2)
* `Appendix`: Includes a program used to generate the input data for the experiments (see the Appendix of our paper for details)
* `data`: Contains the input data used for the experiments and the corresponding results
  * `inputs`: Data sets used in the experiments
* `results`: Full details of the results of Experiments 1, 2 and 3

## Usage

### Environment set-up

First, clone this repository to your local machine and access the main directory using the command below:
```terminal
git clone https://github.com/hayamizu-lab/tree-child-orienter.git
cd tree-child-orienter
```
To run the program of TC-orientation-heuristic, use:
```
python TC-orientation-heuristic.py
```
and follow the instructions in tutorial.  
To run the program of TC-orientation, use:
```
python TC-orientation.py
```
and follow the instructions in tutorial.  
To run the program of of TC-orientation-bruteforce-huber2024, use:
```
python TC-orientation-bruteforce-huber2024.py
```
and follow the instructions in tutorial.

### Prerequisites
To run this project, you may require the following packages:
+ sys
+ numpy
+ networkx
+ matplotlib
+ networkx
+ csv
+ itertools
+ time

### Tutorial
When you run the code, you will be prompted for a file name of the input. The input must be a CSV file representing the adjacency matrix of an undirected binary phylogenetic network. Here, we demonstrate the code using `sample-input.csv`, so we enter 'sample-input' (without the extension). Then, you will get the results as follows. In the case when the input network is tree-child orientable, the program will also output a visualisation of its tree-child orientation in PDF format (see `sample-output.pdf`). 
```
File Name: sample-input
Elapsed time: 0.274124104 [sec]
TC-Orientability: YES
```
[sample-output.pdf](sample-output.pdf)

#### Notes
+ With `Appendix/generate-binary-graphs.py` you can generate undirected binary phylogenetic networks at random.
+ By default, the reference to the input file and the destination of the output graph are set to the working directory. If you want to change this, add an absolute or relative path as shown below.
    - References to input files
    ```python
    with open('/path/to/your/output/directory/' + filename + '.csv', 'r', encoding='utf-8') as file:
    ```
    - Save output graph to
    ```python
    plt.savefig('/path/to/your/output/directory/' + filename + '.pdf', format='pdf') 
    ```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding this project, please feel free to contact the authors:

- Tsuyoshi Urata: [uratsuyo244@moegi.waseda.jp](mailto:uratsuyo244@moegi.waseda.jp)
- Manato Yokoyama: [mana.aki.aya@akane.waseda.jp](mailto:mana.aki.aya@akane.waseda.jp)
- Momoko Hayamizu (Corresponding author): [hayamizu@waseda.jp](mailto:hayamizu@waseda.jp)
