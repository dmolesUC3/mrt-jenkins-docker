def project = 'CDLUC3/mrt-core2'
def branchApi = new URL("https://api.github.com/repos/${project}/branches")
def branches = new groovy.json.JsonSlurper().parse(branchApi.newReader())

branches.each { branch ->
  def branchName = branch.name
  def jobName = "${project}-${branchName}".replaceAll('/','-')
  job(jobName) {
    scm {
      git("git://github.com/${project}.git", branchName)
    }
    steps {
      maven("package")
    }
  }
}
