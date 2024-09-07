TRANSFORMATIONS = {
    ('Water', 'Air'): 'Storm',
    ('Water', 'Fire'): 'Steam',
    ('Water', 'Earth'): 'Dirt',
    ('Air', 'Fire'): 'Lightning',
    ('Air', 'Earth'): 'Dust',
    ('Fire', 'Earth'): 'Lava'
}


class Element:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if (self.name, other.name) in TRANSFORMATIONS:
            new_element_name = TRANSFORMATIONS[(self.name, other.name)]
        elif (other.name, self.name) in TRANSFORMATIONS:
            new_element_name = TRANSFORMATIONS[(other.name, self.name)]
        else:
            raise ValueError('Unknown combination')
        return Element(new_element_name)


water = Element('Air')
fire = Element('Fire')
try:
    new_element = fire + water
    print(f'{new_element}, {type(new_element)}')
except ValueError as e:
    print(f'Error: {e}')
