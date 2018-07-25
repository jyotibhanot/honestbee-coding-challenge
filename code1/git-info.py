#! /usr/bin/env python

from subprocess import Popen, PIPE
import os

def run_cmd(cmd):
  try:
    clone = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = clone.communicate()
    if output:
      return output.strip()
  except:
    print cmd + ":command failed"
 
def clone_url(url, repo_name):  
  cmd="git clone " + url
  run_cmd(cmd)

def isGitDir(repo_name):
  if os.path.exists(repo_name):
    cmd = "cd repo_name; git -rev-parse --is-inside-work-tree"
    output=run_cmd(cmd)
    if output == 'is-inside-work-tree':
       return True
  return False

def get_latest_commit_details(repo_name):
  cmd = "cd " + repo_name + " && git log --all --format='%aN' | head -1"
  output = run_cmd(cmd)
  author = output

  cmd = "cd " + repo_name + " && git log --all --format='%ad' | head -1"
  output = run_cmd(cmd)
  date = output

  return (author, date)

def repo_exists(repo):
  cmd = "curl -s https://api.github.com/repos/" + repo + " | grep 'Not Found' "
  output = run_cmd(cmd)
  if "Not Found" in str(output):
    return False
  return True
  
def remove_dir(dir_name):
  cmd = "rm -rf " + dir_name
  run_cmd(cmd)

def main():
  print 'Enter List of repos and type "Done" to exit'
  # List of repos
  list_of_repos = []
  while True:
    # Get repo as input
    repo = raw_input().strip()
    if repo.lower() == 'done':
      break
    list_of_repos.append(repo)

  # for each repo in list collect info
  print "repo_name,repo_url,latest_commit_author,latest_commit_date"
  for repo in list_of_repos:
    # Default values
    repo_name = 'None'
    repo_url = 'None'
    latest_commit_author = 'None'
    latest_commit_date = 'None'
    
    # Check if repo exists
    if repo_exists(repo):
      # Convert to git url
      repo_url="https://github.com/" + repo + ".git"
      # Get repo dir name
      repo_name=repo.split('/')[1]
      # Check for git dir
      if isGitDir(repo_name):
        run_cmd("git pull")
      else:
        clone_url(repo_url, repo_name)
      # Get latest commit author and date
      latest_commit_author, latest_commit_date = get_latest_commit_details(repo_name)
      remove_dir(repo_name)

    print "%s,%s,%s,%s" % (repo_name, repo_url, latest_commit_author, latest_commit_date)

if __name__ == '__main__':
  main()
