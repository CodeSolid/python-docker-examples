## Running SageMath in a Container:

For more on this source, see the article [Python Docker Examples: SageMath in a Container](https://codesolid.com/python-docker-examples-sagemath-in-a-container/).


## Build the container image from the Dockerfile

```
./build.sh
```

## Running the container with the volume mapped correctly:
```
./run.sh
```

## Launch Jupyter Lab
 Once connected to the container, use:
 ```
 ./run_lab.sh 
 ```
 to launch Jupyter Lab with Sage enabled.  Use the URL that begins with http://127.0.0.1:8888 to connect to sage from a browser on your host machine.  

 As an alternative, you can run the sage console by simply typing sage within the container.
