# Speech-Translation
To build a Docker Image

```docker
docker image build -t speech_trans .
```

Run the container

```docker
docker run -p 5000:5000 -d speech_trans
```
View the APP at port 5000

```basic
localhost:5000
```