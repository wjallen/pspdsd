#!/usr/bin/env python
#
# Protein class hierarchy; contains just the good bits.
#

class Protein:
	def __init__(self):
		self.chain = []
		self.pdbid = ''

	def clean(self):
		del self.chain[:]
		self.pdbid = ''
		

	def print_chains(self):
		for c in range(len(self.chain)):
			print self.chain[c].chainid

	def print_residues(self):
		for c in range(len(self.chain)):
			for r in range(len(self.chain[c].residue)):
				print self.chain[c].chainid + "." + self.chain[c].residue[r].resid

	def print_atoms(self):
		for c in range(len(self.chain)):
			for r in range(len(self.chain[c].residue)):
				for a in range(len(self.chain[c].residue[r].atom)):
					print ( self.chain[c].chainid + "." + 
						self.chain[c].residue[r].resid + "." + 
						self.chain[c].residue[r].atom[a].atomname )


class Chain:
	def __init__(self):
		self.residue = []
		self.chainid = ''

	def clean(self):
		del self.residue[:]
		self.chainid = ''
	
	def print_residues(self):
		for r in range(len(self.residue)):
			print self.residue[r].resid

	def print_atoms(self):
		for r in range(len(self.residue)):
			for a in len(self.residue[r].atom):
				print self.residue[r].resid + "." + self.residue[r].atom[a].atomname


class Residue:
	def __init__(self):
		self.atom = []
		self.resid = ''
		self.resname = ''

	def clean(self):
		del self.atom[:]
		self.resid = ''
		self.resname = ''

	def print_atoms(self):
		for a in range(len(self.atom)):
			print self.atom[a].atomname


class Atom:
	def __init__(self):
		self.atomname = ''
		self.x = ''
		self.y = ''
		self.z = ''

	def clean(self):
		self.atomname = ''
		self.x = ''
		self.y = ''
		self.z = ''


