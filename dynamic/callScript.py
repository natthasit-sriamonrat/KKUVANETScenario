import os
import sys

os.system('python generateBidiDistricts.py kku_maps.net.xml')
os.system('od2trips -c od2trips.config.xml -n kku_maps.net.xml.taz.xml -d OD_file_mon7.od -o od_file.odtrips.xml')
os.system('duarouter -c duarcfg_file.trips2routers.duarcfg -o od_route_file.odtrips.rou.xml --routing-algorithm dijkstra')
