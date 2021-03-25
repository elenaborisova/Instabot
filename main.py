from instapy import InstaPy
from instapy.util import smart_run

details = {
    'username': 'testusername',
    'password': 'testpassword',
    'location': 'c689194/madrid-spain/',
}

tags = ['coding', 'programming', 'python', 'java', 'js', 'javascript', 'ruby',
        'datascience', 'machinelearning', 'artificialintelligence']

users = ['user1', 'user2']

session = InstaPy(
    username=details['username'],
    password=details['password'],
    headless_browser=False,
)

with smart_run(session):
    session.set_relationship_bounds(
        enabled=True,
        potency_ratio=1.25,
        delimit_by_numbers=True,
        max_followers=10000,
        min_followers=300,
        min_following=100,
        min_posts=10,
    )

    session.set_quota_supervisor(
        enabled=True,
        sleep_after=['likes_d', 'follows_d'],
        sleepyhead=True,
        stochastic_flow=True,
        notify_me=True,
        peak_likes_daily=10,
        peak_follows_daily=10,
    )

    session.set_action_delays(
        enabled=True,
        like=5,
        follow=5,
        randomize=True,
        random_range_from=70,
        random_range_to=140)

    session.set_skip_users(skip_private=False, skip_no_profile_pic=False, no_profile_pic_percentage=100)
    session.set_delimit_liking(enabled=True, min_likes=10, max_likes=None)
    session.set_do_follow(enabled=True, percentage=10, times=1)

    session.like_by_tags(tags, amount=10)
    session.like_by_locations([details['location']], amount=10)

    session.accept_follow_requests(amount=10, sleep_delay=1)
    session.follow_user_followers(users, amount=10, randomize=True)
    session.follow_user_following(users, amount=10, randomize=True)

    session.end()
