# Project Network Analytics Fourthbrain - Network Analytics

## This is the docker/container test of our capstone deployment
## it is in the container branch of the repo


For this Capstone project we are using data fron the University of Nevada.

Specifically, their Reno Intrusion Detection Dataset (UNR-IDD).

The main difference between UNR-IDD and other existing datasets is that UNR-IDD consists primarily of network port statistics.

These refer to the observed port metrics recorded in switch/router ports within a networking environment.

The dataset also includes delta port statistics which indicates the change in magnitude of observed port statistics within a time interval.

Compared to datasets that primarily use flow level statistics, these port statistics can provide a fine-grained analysis of network flows from the port level as decisions are made at the port level versus the flow level.

This can lead to rapid identification of potential intrusions.

UNR-IDD also address the limitation of the presence of tail classes.

The dataset ensures that there are enough samples for ML classifiers to achieve high F-Measure scores, uniquely.

Our proposed dataset also ensures that there are no missing network metrics and that all data samples are filled.

* Renato Barroco
* Joaquin Gianantonio

[UNR-IDD-Dataset](https://www.tapadhirdas.com/unr-idd-dataset)
