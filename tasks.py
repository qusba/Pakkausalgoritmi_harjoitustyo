from invoke import task

@task
def testaahuffman(ctx):
	ctx.run("pytest Huffman")
@task
def huffmancoverage(ctx):
	ctx.run("coverage run --branch -m pytest Huffman")
@task(huffmancoverage)
def huffman_coverage_report(ctx):
	ctx.run("coverage html")
