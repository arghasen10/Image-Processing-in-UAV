echo "Bash File running"
arduino --port /dev/ttyMCC --upload ~/Desktop/aetdrone/Image-Processing-in-UAV/aruino-data/aruino-data.ino
echo "Arduino code Uploaded"
echo "Python script started"
python ~/Desktop/aetdrone/Image-Processing-in-UAV/udoo_sensor_data_read.py
echo "Python Script END"
rm /var/opt/m4/m4last.fw





