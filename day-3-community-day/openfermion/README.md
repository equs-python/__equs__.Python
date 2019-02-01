
## Openfermion setup


### Online Notebook
You can find a notebook at the following link:
[https://colab.research.google.com/drive/1kIZY9SWEG6p3pIakJvU-XM6ev50C34Ro](https://colab.research.google.com/drive/1kIZY9SWEG6p3pIakJvU-XM6ev50C34Ro)


### Docker

To use the docker image for open fermion you can enter
```bash
sudo docker run -it -p 8888:8888 openfermion_docker
cd ~
wget https://raw.githubusercontent.com/equs-python/__equs__.Python/master/day-3-community-day/openfermion/open-fermion.ipynb
jupyter-notebook --allow-root --no-browser --port 8888 --ip=0.0.0.0
```

You may remember that `control + shift + v` pastes to the command line and may save you from typing out all of the above.

### Conda

Alternatively, you can use your anaconda environment. Remember to pull:

```bash
$ git pull
```

```bash
$ conda activate openfermion
$ pip install openfermionpyscf
$ pip install openfermioncirq
```

And then you will find the ipython notebook in the `day-3-community-day` directory in the workshop git repository. Simply run `jupyter-notebook` to access it.

If you can't find the notebook, don't forget to `git pull` to update your local copy of the repository.
