from flask import Flask, request, jsonify
import requests, json


app = Flask(__name__)





@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    owner_repo_name = data['owner_repo_name']
    token_token = data['token_token']
    
    commits = fetch_commits(owner_repo_name, token_token)
    commit_details = [fetch_commit_details(owner_repo_name, commit['sha'], token_token) for commit in commits]

    commit_messages_and_code = [
        {
            'message': detail['commit']['message'],
            'files': [{'filename': file['filename'], 'patch': file.get('patch')} for file in detail['files']]
        }
        for detail in commit_details
    ]

    commit_message = json.dumps(commit_messages_and_code[0]['message'])

    commit_code = json.dumps(commit_messages_and_code[0]['files'])
     
    return(jsonify({'commit_message': commit_message, 'commit_code':
                    commit_code})), 200

def fetch_commits(repo_name, token):
    url = f'https://api.github.com/repos/{repo_name}/commits'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commits: {response.status_code} {response.text}")

def fetch_commits(repo_name, token):
    url = f'https://api.github.com/repos/{repo_name}/commits'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commits: {response.status_code} {response.text}")
@app.route('/', methods=['POST'])    
def fetch_commit_details(repo_name, sha, token):
    url = f'https://api.github.com/repos/{repo_name}/commits/{sha}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commit details: {response.status_code} {response.text}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)
