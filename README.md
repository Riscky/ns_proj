# Community discovery in large networks

The scripts listed in this package are used to perform experiments with different community detection algorithms on large networks.

## Dependencies

Install the following packages for your operation system:

- Python 3.8
- Pipenv

Then, run pipenv to fetch the relevant python packages:

``` bash
pipenv install
```

## Running

The graph generation script can be run with:

``` bash
pipenv run python3 generate.py
```

This will fill a folder `graphs` with graphs in different sizes.
Warning: with the parameters that are currently set this takes up to 13 Gb of disk space.

The algorithms can be run on all generated graphs with the following command:

``` bash
pipenv run python3 main.py
```

The results will be output to two files: `graph.csv` and `results.csv`.
Warning: This might cost a lot of time to finish (possibly days)
