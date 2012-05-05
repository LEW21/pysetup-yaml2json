pysetup-yaml2json
=================

A command for pysetup to convert yaml files to json

Configuration
-------------
To enable yaml2json, add following settings to your setup.cfg:

	[global]
	commands =
		pysetup_yaml2json.yaml2json

	[yaml2json]
	files =
		file.yaml

Usage
-----
yaml2json will be automatically run during `pysetup install`, just before resource installation. Alternatively, you can manually run it with `pysetup run yaml2json`.
