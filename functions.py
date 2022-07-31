import moviepy
import os

class Editor:
	def __init__(self,project):
		self.project = project
	def concatfiles(self,videos,scale=(1280,720)):
        scalenew = str(scale[0])+":"+str(scale[1])
		if len(videos) == 0 or len(videos) ==1:
			raise ValueError("Not enough videos!")
		else:
			if len(videos)==2:
				os.system(f"ffmpeg -y -i {videos[0]} -vf scale=1280:720 -preset slow -crf 18 {videos[1]}")
		
