from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {'north': 90, 'south': 270, 'east': 0, 'west': 180}


class Snake:

    def __init__(self):

        self.body_segments = []
        self.start_body()
        self.head_segment = self.body_segments[0]

    def add_body_segment(self, position):
        """Add a new segment to the body at the given position"""
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()

        # Setting up the stating position of each segment
        new_segment.setposition(position)

        self.body_segments.append(new_segment)

    def extend_body(self):
        """Add a new segment to the snake's body at the last segment's position"""
        self.add_body_segment(self.body_segments[-1].position())

    def move_body(self):
        # range() does not accept keyword arguments
        # for i in range(start= len(segments) - 1, stop=0, step=-1)
        for i in range(len(self.body_segments)-1, 0, -1):
            new_position = self.body_segments[i-1].position()
            self.body_segments[i].setposition(new_position)
        self.head_segment.forward(MOVE_DISTANCE)

    def start_body(self):
        """Start the snake's body with 3 of segments at home locations."""
        for position in STARTING_POSITIONS:
            self.add_body_segment(position)

    def up(self):
        if self.head_segment.heading() != DIRECTIONS['south']:
            self.head_segment.setheading(DIRECTIONS['north'])

    def down(self):
        if self.head_segment.heading() != DIRECTIONS['north']:
            self.head_segment.setheading(DIRECTIONS['south'])

    def right(self):
        if self.head_segment.heading() != DIRECTIONS['west']:
            self.head_segment.setheading(DIRECTIONS['east'])

    def left(self):
        if self.head_segment.heading() != DIRECTIONS['east']:
            self.head_segment.setheading(DIRECTIONS['west'])
