from datetime import datetime

from protobuf_inspector.types import StandardParser

from xml.dom import minidom
import os


with open('buf1.txt') as fp:
    root,metadata = None,None
    line = fp.readline()
    cnt = 1
    skip = False
    session_date = ''
    while line:
        try:
            if 'day_session' in line:
                skip = False
                try:
                    xml_str = root.toprettyxml(indent ="\t")
                    save_path_file = "visit-{}.gpx".format(session_date)
                    with open(save_path_file, "w") as f:
                        f.write(xml_str)
                except:
                    pass
                cnt += 1
                root = minidom.Document()
                gpx = root.createElement('gpx')
                root.appendChild(gpx)
                metadata = root.createElement('metadata')
                gpx.appendChild(metadata)
                trk = root.createElement('trk')
                gpx.appendChild(trk)
                trkseg = root.createElement('trkseg')
                trk.appendChild(trkseg)
            elif 'main_timestamp' in line:
                session_date = datetime.utcfromtimestamp(float(line.split('=')[1].strip())).strftime('%Y-%m-%d-%H-%M-%S')
            elif 'location_name' in line:
                name = root.createElement('name')
                text = root.createTextNode(line.split('"')[1].split('"')[0].strip())
                name.appendChild(text)
                root.firstChild.firstChild.appendChild(name)
            elif 'location_list' in line:
                continue
            elif 'gps_location' in line:
                trkpt = root.createElement('trkpt')
                root.lastChild.lastChild.lastChild.appendChild(trkpt)
            elif 'timestamp' in line:
                time = root.createElement('time')
                date_time_object = datetime.utcfromtimestamp(float(line.split('=')[1].strip()))
                time_string = date_time_object.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4]+'Z'
                timestamp = root.createTextNode(time_string)
                time.appendChild(timestamp)
                root.lastChild.lastChild.lastChild.lastChild.appendChild(time)
            elif 'x' in line:
                x = (line.split('=')[1].strip())
                root.lastChild.lastChild.lastChild.lastChild.setAttribute('lat', x)
            elif 'y' in line:
                x = (line.split('=')[1].strip())
                root.lastChild.lastChild.lastChild.lastChild.setAttribute('lon', x)
            elif 'z' in line:
                x = (line.split('=')[1].strip())
                time = root.createElement('ele')
                timestamp = root.createTextNode(x)
                time.appendChild(timestamp)
                root.lastChild.lastChild.lastChild.lastChild.appendChild(time)
            else:
                continue
        finally:
            line = fp.readline()
    try:
        xml_str = root.toprettyxml(indent ="\t")
        save_path_file = "visit-{}.gpx".format(session_date)
        with open(save_path_file, "w") as f:
            f.write(xml_str)
    except:
        pass