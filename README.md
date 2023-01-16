# Operational Technical Test

This is a short technical test to simulate an operational scenario that you might be expected to undertake in your role. This is not meant to take a lot of time to complete or be very complex.

## Prerequisites

This repository contains the code to build a [Docker](https://docs.docker.com/) image. Please follow the instructions available in the Docker documentation to install & configure this on your local machine. 

## Problem Statement

The docker image contained in this repository is a very small [ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) task that is designed to read in recorded temperatures and produce aggregated results on a country level basis. The task utility expects two arguments, the filepath to the source CSV dataset to read and the filepath to where the destination CSV should be output.

There are two files in the `csv` directory, `cities1.csv` & `cities2.csv`. These are the input datasets that we wish to run the task on.

1. Please ensure the Docker image is built with the `temps` tag, e.g. `docker build -t temps .`

2. For each task, please run the docker image with the relevant parameters, e.g:

```
docker run --rm -ti -v $(pwd)/csv:/csv temps /csv/input.csv /csv/output.csv
```

If the task is SUCCESSFUL, please submit the CSV generated with your response to this test.

If the task FAILS, please attempt to determine where this is failing and ascertain why the failure is occurring. You may or may not be able to fix the issue. The objective is to provide written feedback to a development team to aid them understanding why a failure happened so this saves time in developing a solution. Please submit the written results of your investigation into any failed task with your response to this test.
