# Results
This directory contains a summary of the experimental results obtained for some of the networks in `data`.

## Experiment 1
The file `leaf_n10_experiment1.txt` summarises the results of all runs of `TC-orientation-bruteforce-huber2024`, `TC-orientation` and `TC-orientation-heuristic` in Experiment 1 of our paper. The input data are networks with 10 leaves and 2 to 5 reticulations, which can be found in `data/inputs/leaf_n10_experiment1`.   

Each line in the file is of the format

```
input r timeHuber time1 time2
```

where

- `input` is the name of the csv file (adjacency matrix) in `data/inputs` used for the run.
- `r` is the number of reticulations in the input network.
- `timeHuber` is the computation time of `TC-orientation-bruteforce-huber2024` reported by the wall clock time.
- `time1` is the computation time of `TC-orientation` reported by the wall clock time. 
- `time2` is the computation time of `TC-orientation-heuristic` reported by the wall clock time. 

## Experiments 2 and 3
The file `leaf_n10_algo1_vs_algo2.txt` contains the results of all runs in Experiment 2 of our paper. The input data are networks with 10 leaves and 1 to 5 reticulations (i.e. those in `data/inputs/leaf_n10_experiment2/leaf_n10_reticulation_r1` to`r5`).     

The file `leaf_n20_algo1_vs_algo2.txt` contains the results of all runs in Experiment 3 of our paper. The input data are networks with 20 leaves and 1 to 9 reticulations  (i.e. those in `data/inputs/leaf_n20_experiment3/leaf_n20_reticulation_r1` to`r9`). 

Each line in these files is of the format

```
input r time1 time2 result1 result2
```

where

- `input` is the name of the csv file (adjacency matrix) in `data/inputs` used for the run.
- `r` is the number of reticulations in the input network.
- `time1` is the computation time of `TC-orientation` reported by the wall clock time. (We have omitted the time taken for the NO instances with n = 20 and r = 9.)
- `time2` is the computation time of `TC-orientation-heuristic` reported by the wall clock time. (We have omitted the time taken for the NO instances with n = 20 and r = 9.)
- `result1` is `YES` if `TC-orientation` outputs a tree-child orientation of the input, and `NO` otherwise.
- `result2` is `YES` if `TC-orientation-heuristic` outputs a tree-child orientation of the input, and `NO` otherwise.
