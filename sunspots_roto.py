from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

file = open("predicted-sunspot-radio-flux.txt", 'r')
data = []
for line in file.readlines():
    if not (line[0] == ':' or line[0] == '#') :
        data.append(line.split())

drawing = Drawing(200, 150)

pred = [float(row[4])-40 for row in data]
high = [float(row[5])-40 for row in data]
low = [float(row[6])-40 for row in data]
times = [200*((float(row[0]) + float(row[1])/12) - 2015) - 110 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), stroleColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')