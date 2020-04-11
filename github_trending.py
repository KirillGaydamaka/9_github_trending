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
    repos_info = get_trending_repositories(20)
    for repo in repos_info:
        stars = repo['stargazers_count']
        owner = repo['owner']['login']
        name = repo['name']
        html_url = repo['html_url']
        open_issues_amount = get_open_issues_amount(owner, name)
        print(name, stars, open_issues_amount, html_url)
