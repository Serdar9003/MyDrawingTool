import FreeCAD
import Part

class MyDrawingTool:
    def register(self):
        FreeCAD.Console.PrintMessage("MyDrawingTool is registered\n")

    def draw_line(self, start_point, end_point):
        line = Part.LineSegment(FreeCAD.Vector(start_point), FreeCAD.Vector(end_point))
        Part.show(line.toShape())
        FreeCAD.Console.PrintMessage(f"Line drawn from {start_point} to {end_point}\n")

    def draw_rectangle(self, corner_point, width, height):
        rect = Part.makePolygon([
            FreeCAD.Vector(corner_point),
            FreeCAD.Vector(corner_point[0] + width, corner_point[1], corner_point[2]),
            FreeCAD.Vector(corner_point[0] + width, corner_point[1] + height, corner_point[2]),
            FreeCAD.Vector(corner_point[0], corner_point[1] + height, corner_point[2]),
            FreeCAD.Vector(corner_point)
        ])
        Part.show(rect)
        FreeCAD.Console.PrintMessage(f"Rectangle drawn at {corner_point} with width {width} and height {height}\n")

    def draw_circle(self, center_point, radius):
        circle = Part.Circle()
        circle.Center = FreeCAD.Vector(center_point)
        circle.Radius = radius
        Part.show(circle.toShape())
        FreeCAD.Console.PrintMessage(f"Circle drawn at {center_point} with radius {radius}\n")
