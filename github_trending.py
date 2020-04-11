import requests
import datetime


def get_trending_repositories(top_size):
    target_date = datetime.date.today() - datetime.timedelta(days=7)
    payload = {
        'q': 'created:>{}'.format(target_date),
        'sort': 'stars',
        'order': 'desc'
    }
    url = 'https://api.github.com/search/repositories'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    response = requests.get(url)
    response.raise_for_status()
    return len(response.json())


if __name__ == '__main__':
    top_size = 20
    repos_info = get_trending_repositories(top_size)
    for repo in repos_info:
        repo_stars = repo['stargazers_count']
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_html_url = repo['html_url']
        open_issues_amount = get_open_issues_amount(repo_owner, repo_name)
        print(repo_name, repo_stars, open_issues_amount, repo_html_url)
