from invoke import task

@task
def testaahuffman(ctx):
	ctx.run("pytest Huffman")
