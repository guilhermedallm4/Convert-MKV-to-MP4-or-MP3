"""
command FFMPEG complet
FFMPEG -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 "SAIDA"

command FFMPEG simplifated
FFMPEG -i "INPUT" "OUTPUT" 
"""

from mimetypes import common_types
import os
import sys
sys.stdin.reconfigure(encoding='utf-8') #refactore input encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8') #refactore output encoding to utf-8

commando_ffmpeg = r'Path\ffmpeg.exe' #vprogram the way ffmpeg.exe

way_origin = 'C:\Musicas_avk' #Path of origin of archive

for source, paths, archives in os.walk(way_origin): 
    for archive in archives:
        way_complet = os.path.join(source, archive) #Concat the source and archive
        name_archive = os.path.splitext(archive) #Push name archive
        file_input = f'path{name_archive}.extension' #Path of origin archive
        file_output = f'D:\{name_archive}.extension' #Path of destini archive
        command = f'{commando_ffmpeg} -y -i "{file_input}" "{file_output}"' #Command of execute of ffmpeg
        os.system(command) #Execute a command
        


