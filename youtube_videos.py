import requests as rq
from urllib.parse import unquote

link=str(input('Link: '))
print()
if link.find('?v=')!=-1:
	v_id=link[link.find('?v=')+3:]
else:
	v_id = link[link.rfind('/')+1:]

a=rq.get('https://www.youtube.com/get_video_info?video_id='+v_id)
links=unquote(a.text)
name=links[links.find('"videoDetails":{')+len('"videoDetails":{'):]
name=name[name.find('"title":"')+len('"title":"'):]
name=name[:name.find('",')]
links=links.split(',"url":"https://')
del links[0]

count=1
extension=[]
for i in links:
	#params
	params=i[i.find('","mimeType":"')+len('","mimeType":"'):]

	#Type
	Type=params[:params.find(';')]

	#extension
	extension.append(Type[Type.find('/')+1:])

	#bitrate
	bitrate=params[params.find(',"bitrate":')+len(',"bitrate":'):]
	bitrate=bitrate[:bitrate.find(',"')]

	#audioQ
	audioQ=params[params.find(',"audioQuality":"')+len(',"audioQuality":"'):]
	audioQ=audioQ[:audioQ.find('","')]

	#width
	width=params[params.find(',"width":')+len(',"width":'):]
	width=width[:width.find(',')]

	#height
	height=params[params.find(',"height":')+len(',"height":'):]
	height=height[:height.find(',')]

	#contentLength
	contentLength=params[params.find(',"contentLength":"')+len(',"contentLength":"'):]
	contentLength=contentLength[:contentLength.find('",')]

	#quality
	quality=params[params.find(',"quality":"')+len(',"quality":"'):]
	quality=quality[:quality.find('",')]

	#fps
	fps=params[params.find(',"fps":')+len(',"fps":'):]
	fps=fps[:fps.find(',"')]

	#qualityLabel
	qualityLabel=params[params.find(',"qualityLabel":"')+len(',"qualityLabel":"'):]
	qualityLabel=qualityLabel[:qualityLabel.find('",')]

	if Type[len(Type)-1:len(Type)]=='}':
		Type=Type[:-1]
	if bitrate[len(bitrate)-1:len(bitrate)]=='}':
		bitrate=bitrate[:-1]
	if audioQ[len(audioQ)-1:len(audioQ)]=='}':
		audioQ=audioQ[:-1]
	if width[len(width)-1:len(width)]=='}':
		width=width[:-1]
	if height[len(height)-1:len(height)]=='}':
		height=height[:-1]
	if contentLength[len(contentLength)-1:len(contentLength)]=='}':
		contentLength=contentLength[:-1]
	if quality[len(quality)-1:len(quality)]=='}':
		quality=quality[:-1]
	if fps[len(fps)-1:len(fps)]=='}':
		fps=fps[:-1]
	if qualityLabel[len(qualityLabel)-1:len(qualityLabel)]=='}':
		qualityLabel=qualityLabel[:-1]

	no_audio=1
	if i.find(',"audioQuality":"')!=-1:
		no_audio=0
	if no_audio==0:
		print('FILE №'+str(count))
	else:
		print('FILE №'+str(count)+' (NO AUDIO!)')
	if i.find('","mimeType":"')!=-1:
		print('Type:',Type)
	if i.find(',"bitrate":')!=-1:
		print('Bitrate:',bitrate)
	if i.find(',"audioQuality":"')!=-1:
		print('Audio Quality:',audioQ)
	if i.find(',"width":')!=-1:
		print('Width:',width)
	if i.find(',"height":')!=-1:
		print('Height:',height)
	if i.find(',"contentLength":"')!=-1:
		print('Content Length:',contentLength,'bytes')
	if i.find(',"quality":"')!=-1:
		print('Quality:',quality)
	if i.find(',"fps":')!=-1:
		print('FPS:',fps)
	if i.find(',"qualityLabel":"')!=-1:
		print('Quality Label:',qualityLabel)
	print('\n')
	count+=1

if len(links)==0:
	print('The link is incorrect!')
	input()
else:
	while 1:
		ans=str(input('Number: '))
		try:
			ans=int(ans)
			if ans < len(links)+1 and ans > 0:
				break
			else:
				print('ERROR! TRY AGAIN')
		except:
			print('ERROR! TRY AGAIN')

	link='https://'+links[ans-1]
	link=link[:link.find('","mimeType":"')]
	link=link.replace(r'\u0026','&')

	print('Download...')
	a=rq.get(link)
	if extension[ans-1]=='':
		extension='mp4'

	f=open(name+'.'+extension[ans-1],'wb')
	f.write(a.content)
	f.close()

	print('Done!')