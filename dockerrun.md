## file to keep track of the docker runs of the same image: captest-pipreq2

docker run -d -i --name capcont-pipreq2i  -p 8000:8000 captest-pipreq2
docker run -d -i -t --name capcont-pipreq2it  -p 8000:8000 captest-pipreq2 #with this run i get the swagger interface to 'wait' for an input, but i do not know where to enter it...  after i close the run it shows that it was expecting the entry but it never came

I may need to create another image...  with a 

but I will start experimenting with it in another branch of this branch...  "container-sub"