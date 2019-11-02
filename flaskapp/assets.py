from flask_assets import Bundle


def get_assets():
    bundles = {
        'common_css': Bundle(
            'css/common.css',
            'css/navbar.css',
            output='public/common.css',
            filters='cssmin'
        ),
        'common_js': Bundle(
            'js/common.js',
            'js/navbar.js',
            output='public/common.js',
            filters='jsmin'
        ),
        'home_css': Bundle(
            'css/home.css',
            output='public/home.css',
            filters='cssmin'
        ),
        'home_js': Bundle(
            'js/home.js',
            output='public/home.js',
            filters='jsmin'
        ),
    }
    return bundles
