import pyqrcode
from pyqrcode import QRCode


email = 'benikhaleh@gmail.com'

url = pyqrcode.create(email)

url.svg('myqr.svg', scale = 8)
