from invoke import task

@task
def testaa(ctx):
	ctx.run("pytest src/testit")
@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest src/testit")
@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def start(ctx):
	ctx.run("python3 src/index.py")
