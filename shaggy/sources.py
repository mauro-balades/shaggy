
sources = {
    "Telegram": {
        "errorMsg": "<meta property=\"og:description\" content=\"\">",
        "url": "https://t.me/{}",
        "urlMain": "https://telegram.org/",        
    },
    "Instagram": {
        "errorMsg": "Sorry, this page isn't available",
        "url": "https://www.instagram.com/{}",      
    },
    "Facebook": {
        "url": "https://www.Facebook.com/{}",    
        "api": "https://graph.facebook.com/{}/picture",
        "errorCode": 404
    },
    "GitHub": {
        "errorCode": 404,
        "url": "https://www.github.com/{}",
    },
    "GitLab": {
        "errorMsg": "[]",
        "url": "https://gitlab.com/{}",
        "api": "https://gitlab.com/api/v4/users?username={}",
    },
    "Gitee": {
        "errorCode": 404,
        "url": "https://gitee.com/{}",
    },
}
