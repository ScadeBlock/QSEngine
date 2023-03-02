!! WARNING: This project has been closed.
QSEngine on Beta version! You can helps me for develop this Engine!
# QSEngine 0.0.1 Beta
A canvas engine makes with flask and pillow in python. It'll makes a image from server then send it to user computer.
# Document
.JS File
This is a example of JS(QJS) file:

```
@QS.init;

@QS.setscreenupt:50;

@Script.add:machine;

@Machine.load:machine;

@QS.initdata;

@QS.run;
```
`@QS.init` : Init engine

`@QS.setscreenupt:<number>` : Init fps for user 

`@Script.add:<python-filename>` : Add a script

`@Script.load:<python-filename>` : Load a script added

`@Machine.load:<python-filename>` : Use a loaded script to a machine

`@QS.initdata` : add all data loaded to qsmachine

`@QS.run` : Start Server

Python Machine
```
from PIL import Image, ImageDraw
class Machine():
	def __init__(self,IDVALUE):
		super(Machine, self).__init__()
		self.IDVALUE = IDVALUE
	def first_load(self):		
		im = Image.new('RGB', (500, 300), (128, 128, 128))
		draw = ImageDraw.Draw(im)
		draw.rectangle((10, 10, 50,50), fill=(0, 192, 192), outline=(255, 255, 255))
		im.save("./static/"+self.IDVALUE+'.jpg', quality=95)
	def click(self,x,y):
		print(x,y)
```
*First Load is render the first image for user
*Click event
