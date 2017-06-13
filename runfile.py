import sublime
import sublime_plugin

import os

def run_python(file):
	os.system('start ipython3 --no-banner --pdb -i %s' % file)

class RunFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		run_python(self.view.file_name())
