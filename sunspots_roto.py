from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label

file = open("predicted-sunspot-radio-flux.txt", 'r')
data = []
for line in file.readlines():
    if not (line[0] == ':' or line[0] == '#') :
        data.append(line.split())

drawing = Drawing(400, 150)

pred = [float(row[4])-40 for row in data]
high = [float(row[5])-40 for row in data]
low = [float(row[6])-40 for row in data]
# times = [200*((float(row[0]) + float(row[1])/12) - 2015) - 110 for row in data]
times = [float(row[0]) + float(row[1])/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 15
lp.height = 125
lp.width = 300
lp.data = [zip(times,pred), zip(times,high), zip(times,low)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots',
                   fontsize=14, fillColor=colors.red))
# drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
# drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
# drawing.add(PolyLine(zip(times, low), stroleColor=colors.green))
# drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')