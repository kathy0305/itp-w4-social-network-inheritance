from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text=text
        self.timestamp = timestamp or datetime.now()
            
    def set_user(self, user):
        self.user = user  

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        self.user = None
        super(TextPost,self).__init__(text,timestamp)

    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp.strftime('%A, %b %d, %Y'))
##'@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017')

class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.image_url = image_url
        super(PicturePost, self).__init__(text,timestamp)
        
#'@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017')

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp.strftime('%A, %b %d, %Y'))

#'@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'

class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.latitude=latitude
        self.longitude=longitude
        super(CheckInPost,self).__init__(text,timestamp)

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude ,self.timestamp.strftime('%A, %b %d, %Y'))

#'@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'

#https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

#PYTHONPATH=. py.test tests/test_filename.py::TestCaseClassName::individual_test_name