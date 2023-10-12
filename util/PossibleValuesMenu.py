from typing import List
from enum import Enum
from typing import LiteralString, Literal

only_full_menu = ['defect solid stereo', 'defect solid biopsy', 'defect solid tomo',
                  'x-ray uniformity stereo',
                  'x-ray uniformity biopsy', 'x-ray uniformity tomo']
ES_menu = ['x-ray uniformity ES']

list_values = Literal[
    'offset', 'defect', 'defect solid', 'pixel defect',
    'shading', 'x-ray uniformity', 'defect solid stereo', 'defect solid biopsy',
    'defect solid tomo', 'x-ray uniformity stereo',
    'x-ray uniformity biopsy', 'x-ray uniformity tomo', 'x-ray uniformity ES'
]


class PossibleValuesMenu(str, Enum):
    offset = 'offset'
    defect = 'defect'
    defect_solid = 'defect solid'
    pixe_defect = 'pixel defect'
    shading = 'shading'
    uniformity = 'x-ray uniformity'
    defect_solid_stereo = 'defect solid stereo'
    defect_solid_bpy = 'defect solid biopsy'
    defect_solid_tomo = 'defect solid tomo'
    uniformity_stereo = 'x-ray uniformity stereo'
    uniformity_bpy = 'x-ray uniformity biopsy'
    uniformity_tomo = 'x-ray uniformity tomo'
    es_menu = 'x-ray uniformity ES'
