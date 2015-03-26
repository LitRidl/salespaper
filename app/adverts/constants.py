# -*- coding: utf-8 -*-

# _USED = {
#     'new':  0,
#     'used': 1,
#     'crashed': 2
# }

# _TRANSMISSION = {
#     'mechanic': 0,
#     'automatic': 1
# }

# _DRIVE = {
#     'front': 0,
#     'rear': 1,
#     'fourwheel': 2
# }

USED = ('new', 'used', 'crashed')
USED_CHOICES = [
    ('new', 'New'),
    ('used', 'Used'),
    ('crashed', 'Crashed')
]

TRANSMISSION = ('mechanic', 'automatic')
TRANSMISSION_CHOICES = [
    ('mechanic', 'Mechanic'),
    ('automatic', 'Automatic')
]

DRIVE = ('front', 'rear', 'fourwheel')
DRIVE_CHOICES = [
    ('front', 'Front'),
    ('rear', 'Rear'),
    ('fourwheel', '4-wheel')
]
