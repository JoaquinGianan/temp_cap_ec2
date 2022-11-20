## file to keep track of the new docker runs in the container-sub branch of temp-cap-ec2 repo

docker build -t <name for image> .

docker run -d -i -t --name <name for docker>  -p 8000:8000 <name of image>

docker run -d -i --name capcont-pipreq2i  -p 8000:8000 captest-pipreq2
docker run -d -i -t --name capcont-pipreq2it  -p 8000:8000 captest-pipreq2 #with this run i get the swagger interface to 'wait' for an input, but i do not know where to enter it...  after i close the run it shows that it was expecting the entry but it never came

I may need to create another image...  with an  ENTRYPOINT command in the docker file...

but I will start experimenting with it in another branch of this branch...  "container-sub"

will be working on the above issues

calling the images captest-sub-01 and so on
calling the containers capcont-sub-it and so on
