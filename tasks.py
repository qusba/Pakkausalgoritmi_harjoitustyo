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
@task
def testaaLZW(ctx):
	ctx.run("pytest Lempel-Ziv-Welch")
@task
def LZWcoverage(ctx):
	ctx.run("coverage run --branch -m pytest Lempel-Ziv-Welch")
@task(LZWcoverage)
def LZW_coverage_report(ctx):
	ctx.run("coverage html")
