# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1
Charlie Welland
- team member 2
Charlotte Kroll

## Lab Question Answers

1: It would be worthwhile to offload one or both of the processing tasks to your PC if the calculations needed to be done required an immense amount of processing power and the time it would take 
the RPI to complete these tasks would be significantly longer than that of a PC. However, it does take time to transfer data from RPI to PC. Therefore, even though the processing power of the PC 
maybe stronger and the calculation would be completed faster, the time to transmit the data to and from the RPI and the PC would overall take longer than just performing the calculation locally. 

2: The thread.join() is used to wait for the offloaded function offload_process1() to complete before proceeding with the execution of the main thread.

3: The processing functions are executing concurrently, not in parallel. Concurrency means multiple tasks are being executed in overlapping time intervals, while parallelism means multiple tasks 
are being executed simultaneously.

4: The best offloading mode would depend on various factors such as the specific requirements of the application, the available resources, network conditions, and the performance characteristics 
of the processing functions and the server. In this code, the offloading mode with the least execution time would be considered the best.

5: The worst offloading mode would be the one with the lowest execution.

6: Real-world processing functions that involve heavy computations or data-intensive operations are more likely to be offloaded to a server for faster and efficient processing. Examples include 
machine learning model training, image or video processing, and data analytics. Offloading these functions to a server can help reduce the computational load on the local machine and improve 
overall performance.
