from fabric import Connection, task

CONNECTION_PROPERTIES = {
    "host": "18.118.255.26",
    "user": "ubuntu",
    "connect_kwargs": {
        "key_filename": "/home/ubuntu/bicho/llaveSA.pem"
    },
}


@task
def installback(ctx):
    ctx.run("sudo docker pull 1803sergiosilva/backendactualizarproducto:latest")
    ctx.run("sudo docker run -d -p 3003:3003 1803sergiosilva/backendactualizarproducto:latest")

    ctx.run("sudo docker pull 1803sergiosilva/backendcrearproducto:latest")
    ctx.run("sudo docker run -d -p 3000:3000 1803sergiosilva/backendcrearproducto:latest")

    ctx.run("sudo docker pull 1803sergiosilva/backendeliminarproducto:latest")
    ctx.run("sudo docker run -d -p 3001:3001 1803sergiosilva/backendeliminarproducto:latest")

    ctx.run("sudo docker pull 1803sergiosilva/backendordenes:latest")
    ctx.run("sudo docker run -d -p 3004:3000 1803sergiosilva/backendordenes:latest")

    ctx.run("sudo docker pull 1803sergiosilva/backendusuarios:latest")
    ctx.run("sudo docker run -d -p 3005:3000 1803sergiosilva/backendusuarios:latest")

    ctx.run("sudo docker pull 1803sergiosilva/backendverproducto:latest")
    ctx.run("sudo docker run -d -p 3002:3002 1803sergiosilva/backendverproducto:latest")

    print("Lanzamiento de instancias terminado")

@task
def deploy(ctx):
    with Connection(**CONNECTION_PROPERTIES) as c:
        installback(c)
