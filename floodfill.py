class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):

        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def fill(image, coordinate, color):

    coord = Point(*coordinate)
    w, h = image.shape[:2]
    dir4 = [Point(0, -1), Point(-1, 0), Point(0, 1), Point(1, 0)]
    q = []
    q.append(coord)
    print("Starting....")
    while(len(q) > 0):
        p = q.pop(0)
        for d in dir4:
            next = p + d
            if (next.x >= 0 and next.x < w and next.y >= 0 and next.y < h):
                if (image[next.x][next.y][0] == 0 and
                        image[next.x][next.y][1] == 0
                        and image[next.x][next.y][2] == 0):
                    image[next.x][next.y] = color
                    q.append(next)
    print("Complete")


def fill_multiple(image, coordinateList, color):

    for i in coordinateList:
        coord = Point(*i)
        w, h = image.shape[:2]
        dir4 = [Point(0, -1), Point(-1, 0), Point(0, 1), Point(1, 0)]
        q = []
        q.append(coord)
        print("Starting....")
        while(len(q) > 0):
            p = q.pop(0)
            for d in dir4:
                next = p + d
                if (next.x >= 0 and next.x < w and next.y >= 0 and next.y < h):
                    if (image[next.x][next.y][0] == 0 and
                            image[next.x][next.y][1] == 0
                            and image[next.x][next.y][2] == 0):
                        image[next.x][next.y] = color
                        q.append(next)
        print("Complete")
