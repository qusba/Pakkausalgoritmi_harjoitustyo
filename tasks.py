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
def testaaLZW(ctx):
	ctx.run("pytest src/testit/LZW_testit")
@task
def LZWcoverage(ctx):
	ctx.run("coverage run --branch -m pytest src/testit/LZW_testit")
@task(LZWcoverage)
def LZW_coverage_report(ctx):
	ctx.run("coverage html")
