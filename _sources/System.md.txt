# System Overview

The system is setup to facilitate parallel research and engineering work on multiple "thrusts" of the project.

<!-- ```{toctree}
:maxdepth: 2

System/Hardware.md
System/Software.md
System/RobotSkills.md
System/RobotTasks.md

``` -->

```{contents}
```

## Hardware

The diagram below shows how various equipment, sensors and virtual machines are connected to one another. Few key points to note:

* The physical hardware of the cloud infrastructure is on CMU main campus
* Mezzanine Lab equipment is located at Mill19 campus of CMU

![hardware](files/system-hardware.png)

## Software

Simplified view of the integrated system software stack is given below.

*work in progress*

![software-simple](files/system-software-simple.png)

## Task Execution

A manufacturing task, like inserting a male connector to a female connector, is executed by using both vision and vibrotactile skills of the system. Below is a high-level flow diagram of how different skills are executed to fulfill a task to assemble a connector.

![system-tasks](files/system-tasks.png)