import yaml
import json

from distutils2.command.cmd import Command
from distutils2.config import get_resources_dests

from distutils2.command.install_dist import install_dist

def monkey():
	i = 0
	found = False
	for cmd, check in install_dist.sub_commands:
		if cmd == "install_data":
			found = True
			break

		i = i + 1

	if found:
		install_dist.sub_commands.insert(i, ("yaml2json", lambda self: True))

monkey()

def recode(ya, js):
	if isinstance(ya, basestring):
		ya = open(ya)

	if isinstance(js, basestring):
		js = open(js, "w")

	json.dump(yaml.load(ya), js)

class yaml2json(Command):
	user_options = []

	def initialize_options(self):
		self.files = None
		pass

	def finalize_options(self):
		pass

	def run(self):
		files = get_resources_dests(".", [('', glob.strip(), '') for glob in self.files.strip().split("\n")])
		for file in files:
			recode(file, file.replace(".yaml", ".json"))

		# Reload the configuration, so wildcards in resources will detect json files.
		self.distribution.parse_config_files()
