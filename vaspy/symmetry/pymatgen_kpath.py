# coding: utf-8
# Copyright (c) Scanlon Materials Theory Group
# Distributed under the terms of the MIT License.

from vaspy.symmetry import Kpath

from pymatgen.symmetry.bandstructure import HighSymmKpath


class PymatgenKpath(Kpath):
    """Calculate the high-symmetry k-point path using pymatgen.

    More detail on the paths generated by SeeK-path can be found in the
    pymatgen documentation. They are based on the paper:
    Setyawan, W., & Curtarolo, S. (2010) High-throughput electronic band
    structure calculations: Challenges and tools. Computational Materials
    Science, 49(2), 299-312. doi:10.1016/j.commatsci.2010.05.010

    These paths should be used with primitive structures that comply with the
    definition from the paper. This structure can be accessed using the
    `prim` attribute and compliance between the provided structure and
    standardised structure checked using the `correct_structure` method.

    Args:
        structure (Structure): A pymatgen structure object.
        symprec (float): The tolerance for determining the crystal symmetry.

    Attributes:
        kpoints (dict): The high-symmetry k-point labels and their coordinates
            as {label: coords}.
        path (list): The high-symmetry k-point path. Each subpath is provided
            as a list. E.g. [['A', 'B'], ['C', 'D']].
        prim (Structure): The standardised primitive cell structure needed for
            to obtain the correct band structure.
        conv (Structure): The standardised conventional cell structure.
        lattice_type (str): The Bravais lattice system. Hexagonal cells are
            separated into rhombohedral and hexagonal lattices.
        spg_symbol (str): The international space group symbol.
        spg_number (int): The international space group number.
        path_string (str): The high-symmetry k-point path formatted with arrows
            and showing disconnections between subpaths. For example:
            "X -> Gamma | Y -> Z".
    """

    def __init__(self, structure, symprec=1e-3):
        Kpath.__init__(self, structure, symprec=symprec)
        pmg_path = HighSymmKpath(structure, symprec=symprec)
        self._kpath = pmg_path._kpath
        self.prim = pmg_path.prim
        self.conv = pmg_path.conventional
