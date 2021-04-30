Flask Challenge
===============

For simple API using flask

```bash
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-dev
```

1. Clone the project form Github

```bash
$ git clone https://github.com/izaazira/flask-challenge.git
$ cd flask-challenge
$ cd /api/config.py.example /api/config.py
```

2. Copy and update your config file.
```bash
$ cd /api/config.py.example /api/config.py
```

This project already include a docker and also docker-compose. It is a yeah for you.

3. Next, you need to install docker. Feel free to find any platform that easy for you. Since I am using ubuntu 18.04, I used [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) tutorial for setup.

3. Then you need to deploy the database first.
```bash
$ python3 api/database.py -d
```

4. Build the docker file and run it.
```bash
$ docker build -t flask-challenge:latest .
$ docker-compose up
```
Now your API is up with port 5000
