import pyqrcode
url="https://github.com/SathishkumarMV"
a=pyqrcode.create(url)
a.svg('github.svg',scale=10)
