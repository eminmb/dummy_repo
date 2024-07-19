import os
import requests
import json
from langchain_community.llms import Ollama

# Function to fetch commits from GitHub
def fetch_commits(repo_owner, repo_name, token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commits: {response.status_code} {response.text}")

# Function to fetch detailed commit data
def fetch_commit_details(repo_owner, repo_name, sha, token):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{sha}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commit details: {response.status_code} {response.text}")

# Function to analyze with Gemma 2 via Ollama
def analyze_with_gemma2(input_text):
    llm = Ollama(model="gemma2")
    response = llm.invoke(input_text)
    return response

# Function to check commit message and code relationship
def check_message_code_relationship(commit_message, commit_code):
    input_text = f"This is the commit message: {commit_message} This is the committed code: {commit_code} Does the commit message accurately and well express what the code does?"
    return analyze_with_gemma2(input_text)

# Example usage
repo_owner = 'eminmb'
repo_name = 'dummy_repo'
github_token = os.getenv('RUN_GEMMA_TOKEN')

# Step 1: Fetch commits
commits = fetch_commits(repo_owner, repo_name, github_token)

# Step 2: Fetch detailed commit data
commit_details = []
for commit in commits:
    sha = commit['sha']
    details = fetch_commit_details(repo_owner, repo_name, sha, github_token)
    commit_details.append(details)

# Extract commit message and committed code
commit_messages_and_code = [
    {
        'message': detail['commit']['message'],
        'files': [{'filename': file['filename'], 'patch': file.get('patch')} for file in detail['files']]
    }
    for detail in commit_details
]

# Step 4: Analyze commit message and code relationship
results = []
for commit in commit_messages_and_code[:1]:  # Display first one for brevity
    commit_message = json.dumps(commit['message'])
    commit_code = json.dumps(commit['files'])
    output_message_code = check_message_code_relationship(commit_message, commit_code)
    result = f"Message-Code Relationship Analysis Input: This is the commit message: {commit_message} This is the committed code: {commit_code}\nOutput: {output_message_code}\n"
    print(result)
    
 with open('my_results.txt', 'w') as f:
    f.write(result)   

