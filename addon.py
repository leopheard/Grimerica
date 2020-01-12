from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "http://www.grimerica.ca/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30002),
            'path': "https://s2.radio.co/s053ed3122/listen",
            'thumbnail': "https://grimerica.ca/wp-content/uploads/2019/08/grimerica-logo.png",
            'is_playable': True},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/dir-logo/258430/258430_300x300.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/dir-logo/258430/258430_300x300.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
