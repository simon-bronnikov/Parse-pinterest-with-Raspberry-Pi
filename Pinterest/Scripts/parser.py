from py3pin.Pinterest import Pinterest
import urllib.request
import config
import subprocess

class Parser:
    def __init__(self):
        self.email = config.EMAIL
        self.passwrod = config.PASSWORD
        self.username = config.USERNAME
        self.cred_root = '../Creds'

    def download_pics(self):
        count = 0
        pins = self._get_home_feed()

        for info in pins:
            count += 1
            url = info["images"]["orig"]["url"]
            image_name = "../Pictures/image" + str(count) + ".png"
            urllib.request.urlretrieve(url, image_name)

    def _get_home_feed(self, max_items=100) -> list:
        pinterest = self._get_pinterest()

        home_feed_pins = []
        home_feed_batch = pinterest.home_feed()

        while len(home_feed_batch) > 0 and len(home_feed_pins) < max_items:
            home_feed_pins += home_feed_batch
            home_feed_batch = pinterest.home_feed()
        
        return home_feed_pins
    
    
    def _get_pinterest(self):
        pinterest = Pinterest(email=self.email,
                            password=self.passwrod,
                            username=self.username,
                            cred_root=self.cred_root)
        return pinterest
    

if __name__ == '__main__':
    subprocess.Popen(['fbi', '-a', '--noverbose', '../Pictures/picture.jpg'])
    Parser().download_pics()