### Setting up a virtual environment for Python

A virtual environment for the Python language is a prerequisite for participating in the second part of the workshops, where you will be able to communicate with large language models on the watsonx.ai service from the Jupyter Notebook level.

To set up a virtual environment for Python, you need to have the 'podman' tool on your local machine, as we will use containers to prepare the environment.

If you don't have 'podman' on your local machine, download the installation package from https://podman.io in the "Downloads" section. Then run the installer and follow the instructions for your operating system described at https://podman.io/docs/installation

After successfully installing the ```podman``` tool, open a terminal window and initialize the ```podman``` virtual machine by executing the following sequence of commands:


```
podman machine init
podman machine start
```

Podman uses QEMU, so after executing the commands indicated above, check if the virtual machine is working correctly by executing the following command in the same terminal window:

```
podman machine list 
```

If ```podman``` is ready to work, you should get the following information on the screen:


```
NAME                     VM TYPE     CREATED        LAST UP            CPUS        MEMORY      DISK SIZE
podman-machine-default*  qemu        14 months ago  Currently running  1           2GiB        100GiB
```

If your result looks like the one above, it means we can move on to the next step.

Create a ```Dockerfile``` with the following content:


```
FROM jupyter/base-notebook:latest

RUN pip install --upgrade pip
RUN pip install ibm_watson_machine_learning

EXPOSE 8888

ENTRYPOINT jupyter notebook --ip='*' --NotebookApp.token='' --NotebookApp.password=''

```
The ```Dockerfile``` will be used to build a container image with installed Python libraries.

To build a container image named ```jupyter```, navigate in the terminal to the directory where your newly created ```Dockerfile``` is located and execute the command below:


```
podman build -t jupyter .
```

Then, run the built container:

```
podman run -d --name jupyter -p 8888:8888 jupyter
```

Then check if your container has started correctly:

```
podman ps -a 
```


If the result of the command in the STATUS column shows the UP value, it means the container has started correctly.

Now, in any WEB browser, open the URL: http://localhost:8888 
In the top right corner of the browser, you will find the ```Upload``` button, press it to upload the prepared jupyter notebook prompt_engineering_challenge.ipynb - you can find it in the [GIT repository](/LABS/3_prompt_engineering_via_code/)

After loading the notebook, you are ready to work.

# Next step

Proceed to the next step to start [Lab 1](/LABS/1_prompt_engineering/README.md)
