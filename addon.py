import re
import xbmcgui
import requests

url = 'https://apid.sky.it/vdp/v1/getLivestream?id=2&jsonp=jsonP.queue.jsonP0_1570037187545'
res = requests.get(url)

try:
	streaming_url = 'https://sbshdlu5-lh.akamaihd.net/i/sbshdl_1@810993/master.m3u8?hdnts=st=1583957164~exp=1584043564~acl=/i/*~hmac=1e353be7417c95a775f53b60bbfce7da92317c917c0c6d42e36a7ad282adef96&mux_audio=true'
	thumb_url = 'https://' + re.findall('"img":"https{0,1}://(.*?)"', res.text)[1]
	listitem = xbmcgui.ListItem('MotorTrend')
	listitem.setInfo('video', {'Title': 'MotorTrend'})
	listitem.setArt({ 'thumb': thumb_url})
	xbmc.Player().play(streaming_url, listitem)

except Exception as ex:
	message = 'Eccezione: %s' % ex
	listitem = xbmcgui.ListItem('MotorTrend - Errore')
	listitem.setInfo('video', {'Title': 'Errore nell\' avvio del plugin MotorTrend'})
	listitem.setInfo('video', { 'plot': message })
