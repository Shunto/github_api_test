from github import Github
from github import InputGitAuthor
import requests
from requests.auth import HTTPBasicAuth
import base64

ENCODING = 'utf-8'

user = "Shunto"
email = "shu.410.soccer.s@gmail.com"
access_token = "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"


with open('pygithub_test.py', 'rb') as f:
    byte_content = f.read()
    base64_bytes = base64.b64encode(byte_content)
    base64_string = base64_bytes.decode(ENCODING)
    payload = {"message": "Add pygithub_test.py",
               "author": {"name": user,"email": email},
               "branch": "master",
               "content": base64_string}
    result = requests.put("https://api.github.com/repos/Shunto/github_api_test/contents/pygithub_test.py", auth=HTTPBasicAuth(user, access_token), json=payload)

# using an access token
#g = Github("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")
# Github Enterprise with custom hostname
#g = Github(base_url="https://{GitHubServerName/api/v3", login_or_token="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")
# Not Enterprise
#g = Github(base_url="https://api.github.com", login_or_token="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")
#repo = g.get_user().get_repo("github_api_test")
#print(repo.name)
#repo.create_file("test.txt", "test", "test", branch="master")
#file = repo.get_contents("test.txt", ref="master")
#data = file.decoded_content.decode("utf-8")
#print(data)
#source = repo.get_branch("master")
#data += "\ngithub_api_test"
#def push(path, message, content, branch):
#    author = InputGitAuthor("Shunto", "shu.410.soccer.s@gmail.com")
#    source = repo.get_branch("master")
#    repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)
#    contents = repo.get_contents(path, ref=branch)
#    repo.update_file(contents.path, message, content, contents.sha, branch=branch, author=author)

#push("test.txt", "Add text.txt", data, "test-branch")
body = '''
SUMMARY
PyGithub API test
'''
#repo.create_pull(title="Github API Test PR", body=body, head="test-branch", base="master")
#for repo in g.get_user().get_repos():
#    print(repo.name)
#    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
#    print(dir(repo))
