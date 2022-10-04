from bs4 import BeautifulSoup
import requests as r
from urllib.parse import urljoin, urlparse
import json
from random import randrange
import logging
import praw

_logger = logging.getLogger(__name__)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def can_load_from_iframe(headers):
    headers = dict(headers)

    if headers.get('X-FRAME-OPTIONS', None) is not None:
        return False

    if headers.get('X-Frame-Options', None) is not None:
        return False

    if headers.get('x-frame-options', None) is not None:
        return False

    if headers.get('CONTENT-SECURITY-POLICY', None) is not None:
        if 'frame-ancestors' in headers.get('CONTENT-SECURITY-POLICY'):
            return False

    if headers.get('Content-Security-Policy', None) is not None:
        if 'frame-ancestors' in headers.get('Content-Security-Policy'):
            return False

    if headers.get('content-security-policy', None) is not None:
        if 'frame-ancestors' in headers.get('content-security-policy'):
            return False

    return True


def get_title(soup):
    title = None

    og_title = soup.find('meta', property='og:title')
    if og_title:
        title = og_title.get('content')

    if not title:
        twitter_title = soup.find('meta', property='twitter:title')
        if twitter_title:
            title = twitter_title.get('content')

    if not title:
        title = soup.find('title')
        if title:
            title = title.text

    return title


def get_img_url(soup):
    img_url = None

    og_image = soup.find('meta', property='og:image')
    if og_image:
        img_url = og_image.get('content')

    if not img_url:
        twitter_image = soup.find('meta', property='twitter:image')
        if twitter_image:
            img_url = twitter_image.get('content')

    if not img_url:
        ld_json = soup.find('script', type='application/ld+json')
        if ld_json:
            json_data = json.loads(ld_json.getText())
            image_data = json_data.get('image')
            if (type(image_data) == type({})):
                img_url = image_data.get('url')
            else:
                img_url = image_data

    return img_url


def run_fark_bot():
    _logger.info('run_fark_bot')
    url = 'https://www.fark.com/'
    res = r.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.find_all("tr", {"class": "headlineRow"})

    data = []
    for link in links:
        if len(link['class']) >= 2 and 'id' in link['class'][1]:
            fark_url = link.find('a')['href']
            if 'twitter.com' not in fark_url and 'youtube.com' not in fark_url and 'kuci.org' not in fark_url:
                headline_span = link.find("span", {"class": "headline"})
                comment_count_span = link.find("span", {"class": "icon_comment_count"})

                data.append({
                    'fark_id': link['class'][1],
                    'subtext': headline_span.text[1:],
                    'comment_count': int(comment_count_span.text),
                    'fark_url': fark_url,
                })

    data = sorted(data, key=lambda link: link['comment_count'], reverse=True)
    top_links = data[:30]
    result = []

    for link in top_links:
        try:
            get = r.get(link['fark_url'], headers=headers, timeout=10)
            fark_301_page = BeautifulSoup(get.text, 'html.parser')
            url = fark_301_page.find('a')['href']
            url = urljoin(url, urlparse(url).path)

            res = r.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')

            likes_booster = abs(int(link['comment_count'] / 2) - randrange(0, 20))
            if likes_booster < 10:
                likes_booster += 5

            name = get_title(soup)
            if not name or len(name) < 15:  # page title fetch failed
                continue

            result.append({
                'img_url': get_img_url(soup),
                'url': url,
                'name': name,
                'likes_booster': likes_booster,
                'can_load_iframe': can_load_from_iframe(res.headers),
                'fark_id': link['fark_id']
            })

        except:
            _logger.exception(link)

    return result


def run_slashdot_bot():
    _logger.info('run_slashdot_bot')
    url = 'https://slashdot.org/'
    res = r.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.find_all('h2', {'class': 'story'})

    data = []

    for link in links:
        try:
            data.append({
                'slashdot_id': link.find('span', {'class': 'story-title'}).find('a')['href'].split('/')[-1],
                'url': link.find('a', {'class': 'story-sourcelnk'})['href'],
                'comment_count': int(link.find('span', {'class': 'comment-bubble'}).find('a').text),
                'name': link.find('span', {'class': 'story-title'}).find('a').text,
            })
        except:
            _logger.exception(link)

    data = sorted(data, key=lambda link: link['comment_count'], reverse=True)

    top_links = data[:3]

    for link in top_links:

        likes_booster = abs(int(link['comment_count'] / 2) - randrange(0, 20))
        if likes_booster < 10:
            likes_booster += 5

        link['likes_booster'] = likes_booster
        del link['comment_count']

    return top_links

def run_reddit_bot():
    _logger.info('run_reddit_bot')
    reddit = praw.Reddit(
        client_id="2OWhJf5hpJbsIKoi7Hj6WA",
        client_secret="lvrWQJEsZnq1WDJvcmXEVdHDPpjG7Q",
        user_agent="script",
        username="DirtySpin",
        password="mjv8ferL39V7eK8c",
    )
    subreddit = reddit.subreddit('nottheonion')
    result = []

    for submission in subreddit.hot(limit=10):
        if submission.score > 400:
            result.append({
                'name': submission.title,
                'url': submission.url,
                'likes_booster': abs(submission.score/ 20) if submission.score < 1500 else randrange(70, 120),
                'reddit_id': submission.id
            })

    subreddit = reddit.subreddit('offbeat')
    for submission in subreddit.hot(limit=10):
        if submission.score > 150:
            result.append({
                'name': submission.title,
                'url': submission.url,
                'likes_booster': abs(submission.score/ 20) if submission.score < 1500 else randrange(70, 120),
                'reddit_id': submission.id
            })

    return result


# res = run_reddit_bot()
# pass
