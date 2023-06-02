sources = {
    "Telegram": {
        "errorMsg": '<meta property="og:description" content="">',
        "url": "https://t.me/{}",
        "urlMain": "https://telegram.org/",
    },
    # "Instagram": {
    #     "errorMsg": "Sorry, this page isn't available",
    #     "url": "https://www.instagram.com/{}",
    # },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "api": "https://graph.facebook.com/{}/picture",
    },
    "GitHub": {
        "url": "https://www.github.com/{}",
    },
    "GitLab": {
        "errorMsg": "[]",
        "url": "https://gitlab.com/{}",
        "api": "https://gitlab.com/api/v4/users?username={}",
    },
    "Gitee": {
        "url": "https://gitee.com/{}",
    },
    "ProductHunt": {
        "errorMsg": "We seem to have lost this page",
        "url": "https://www.producthunt.com/@{}",
    },
    "PromoDJ": {
        "url": "http://promodj.com/{}",
    },
    "PyPi": {
        "url": "https://pypi.org/user/{}",
    },
    "Quizlet": {
        "url": "https://quizlet.com/{}",
    },
    "Rajce.net": {
        "url": "https://{}.rajce.idnes.cz/",
    },
    "Rate Your Music": {
        "url": "https://rateyourmusic.com/~{}",
    },
    "Rclone Forum": {
        "url": "https://forum.rclone.org/u/{}",
    },
    "Redbubble": {
        "url": "https://www.redbubble.com/people/{}",
    },
    "Reddit": {
        "errorMsg": "Sorry, nobody on Reddit goes by that name.",
        "headers": {"accept-language": "en-US,en;q=0.9"},
        "url": "https://www.reddit.com/user/{}",
    },
    "Reisefrage": {
        "url": "https://www.reisefrage.net/nutzer/{}",
    },
    "Replit.com": {
        "url": "https://replit.com/@{}",
    },
    "Tellonym.me": {
        "url": "https://tellonym.me/{}",
    },
    "Tenor": {
        "url": "https://tenor.com/users/{}",
    },
    "ThemeForest": {
        "url": "https://themeforest.net/user/{}",
    },
    "TikTok": {
        "url": "https://tiktok.com/@{}",
    },
    "WebNode": {
        "url": "https://{}.webnode.cz/",
    },
    "Weblate": {
        "url": "https://hosted.weblate.org/user/{}/",
    },
    "Weebly": {
        "url": "https://{}.weebly.com/",
    },
    "Whonix Forum": {
        "url": "https://forums.whonix.org/u/{}/summary",
    },
    "Wikidot": {
        "errorMsg": "User does not exist.",
        "url": "http://www.wikidot.com/user:info/{}",
    },
    "Wikipedia": {
        "errorMsg": "centralauth-admin-nonexistent:",
        "url": "https://en.wikipedia.org/wiki/Special:CentralAuth/{}?uselang=qqx",
    },
    "Windy": {
        "url": "https://community.windy.com/user/{}",
    },
    "Wix": {
        "url": "https://{}.wix.com",
    },
    "WolframalphaForum": {
        "url": "https://community.wolfram.com/web/{}/home",
    },
    "WordPress": {
        "errorUrl": "wordpress.com/typo/?subdomain=",
        "url": "https://{}.wordpress.com/",
    },
    "WordPressOrg": {
        "url": "https://profiles.wordpress.org/{}/",
    },
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/{}/"
    },
    "Twitter": {
        "url": "https://twitter.com/@{}",
    },
    "Spotify": {
        "url": "https://open.spotify.com/user/{}"
    },
    "Archive.org": {
        "url": "https://archive.org/details/@{}/"
    },
    "ask.fm": {
        "url": "https://ask.fm/{}"
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{}",
        "headers": {"accept-language": "en-US,en;q=0.9"},
        "errorMsg": ":: Error</title>"
    },
    "Snaptchat": {
        "url": "https://www.snapchat.com/add/{}"
    }
}
