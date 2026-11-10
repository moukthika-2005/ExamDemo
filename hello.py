sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker

sudo --version 
sudo docker pull ubuntu 
sudo docker images 
sudo docker run -dit --name docker-lab-container ubuntu
sudo docker ps -a
sudo docker exec -it docker-lab-container bash
echo "Helo world "
ls
exit 

