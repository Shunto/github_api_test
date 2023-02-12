from github import Github
from github import InputGitAuthor
import requests
from requests.auth import HTTPBasicAuth
import base64

ENCODING = 'utf-8'

user = "Shunto"
email = "shu.410.soccer.s@gmail.com"
access_token = "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"
access_token = "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"

def create_new_file(path, message, repo, branch, user, email, access_token):
    with open(path, 'rb') as f:
        byte_content = f.read()
        base64_bytes = base64.b64encode(byte_content)
        base64_string = base64_bytes.decode(ENCODING)
        payload = {"message": message,
                   "author": {"name": user,"email": email},
                   "branch": branch,
                   "content": base64_string}
        #url =  f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
        url =  "https://api.github.com/repos/" + user + "/" + repo + "/contents/" + path
        print(url)
        result = requests.put(url, auth=HTTPBasicAuth(user, access_token), json=payload)

create_new_file("pygithub_test.py", "Update pygithub_test.py", "github_api_test", "test-branch", user, email, access_token)
#create_new_file("pygithub_test.py", "update pygithub_test.py", "github_api_test", "master", user, email, access_token)

headers = {'Authorization': "Token " + access_token}
url = "https://api.github.com/repos/Shunto/github_api_test/git/refs/heads"
#r = requests.get(url, headers=headers)
r = requests.get(url, auth=HTTPBasicAuth(user, access_token))
print(r)
branches = requests.get(url, headers=headers).json()
branch, sha = branches[-1]['ref'], branches[-1]['object']['sha']
r = requests.post('https://api.github.com/repos/Shunto/github_api_test/git/refs', json={
    "ref": "refs/heads/new-test-branch",
    "sha": sha
}, headers=headers)
print(r.content)

# using an access token
#g = github("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")
# github enterprise with custom hostname
#g = github(base_url="https://{githubservername/api/v3", login_or_token="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")
# not enterprise
#g = github(base_url="https://api.github.com", login_or_token="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")
#repo = g.get_user().get_repo("github_api_test")
#print(repo.name)
#repo.create_file("test.txt", "test", "test", branch="master")
#file = repo.get_contents("test.txt", ref="master")
#data = file.decoded_content.decode("utf-8")
#print(data)
#source = repo.get_branch("master")
#data += "\ngithub_api_test"
#def push(path, message, content, branch):
#    author = inputgitauthor("shunto", "shu.410.soccer.s@gmail.com")
#    source = repo.get_branch("master")
#    repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)
#    contents = repo.get_contents(path, ref=branch)
#    repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)

#push("test.txt", "add text.txt", data, "test-branch")
body = '''
summary
pygithub api test
'''
#repo.create_pull(title="github api test pr", body=body, head="test-branch", base="master")
#for repo in g.get_user().get_repos():
#    print(repo.name)
#    repo.edit(has_wiki=false)
    # to see all the available attributes and methods
#    print(dir(repo))
