
## Openfermion setup

[https://colab.research.google.com/drive/1kIZY9SWEG6p3pIakJvU-XM6ev50C34Ro](https://colab.research.google.com/drive/1kIZY9SWEG6p3pIakJvU-XM6ev50C34Ro)

To use the docker image for open fermion you can enter
```bash
sudo docker run -it -p 8888:8888 openfermion_docker
cd ~
wget https://raw.githubusercontent.com/equs-python/__equs__.Python/master/day-3-community-day/openfermion/open-fermion.ipynb
jupyter-notebook --allow-root --no-browser --port 8888 --ip=0.0.0.0
```
