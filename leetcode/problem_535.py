class Codec:
    def __init__(self):
        self.urls = {}
        self.arr = []

    def randomString(self):
        result = ''
        for i in range(7):
            result += chr(randint(97, 122))
        return result

    def encode(self, longUrl: str) -> str:
        code = self.randomString()
        baseUrl = 'http://tinyurl.com/'
        self.urls[code] = longUrl
        return baseUrl + code

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.split('/')[-1]
        return self.urls[code]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))