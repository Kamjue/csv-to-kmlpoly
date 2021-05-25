import sys
import csv

print("\n\t** CSV Coords to KML Polygon **\n")

if( len(sys.argv) == 2 and sys.argv[1].endswith(".csv") ):
	with open( sys.argv[1], newline="" ) as csvfile:
		csvreader = csv.reader(csvfile, delimiter=";")
		coords = []
		rowNew = []
		coordsStr = ""

		for row in csvreader:
			rowNew.append(row)

		for row in rowNew[1:]:
			aux = row[2] + "," + row[1]
			coords.append(aux)

		#print(coords)
		coordsStr = "\n".join(coords)

		with open("output.kml", "w") as kmlfile:
			pname = input("Polygon name: ")

			kmlfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n\t<Placemark>\n\t\t<name>" + pname + "</name>\n\t\t<Polygon>\n\t\t\t<extrude>1</extrude>\n\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n\t\t\t<outerBoundaryIs>\n\t\t\t\t<LinearRing>\n\t\t\t\t\t<coordinates>\n" + coordsStr + "\n\t\t\t\t\t</coordinates>\n\t\t\t\t</LinearRing>\n\t\t\t</outerBoundaryIs>\n\t\t</Polygon>\n\t</Placemark>\n</kml>")

else:
	print("\t--** Missing CSV file **--\n")
	# file = open("coord.kml");
	sys.exit()
