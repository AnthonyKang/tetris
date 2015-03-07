import pyscreenshot as ImageGrab
import time
i = 0
while(1):
	#ImageGrab.grab_to_file('grab' + str(i) +'.png')
	img = ImageGrab.grab()
	img.save('grab' + str(i) + '.png')
	img = img.crop()
	print img
	img.save('grab' + str(i) + '.png')
	i = i+1
	time.sleep(1)