import sys, os, getopt

def get_extension(filename):
	extension = filename.split(".")[-1]
	return "." + extension

def get_filename(filename):
	extension = get_extension(filename)
	upto_ext = (len(extension)) * -1
	filename = filename[:upto_ext]
	return filename

def pad(number, padding):
	return str(number).zfill(int("0" + padding))

def handleoptions(actions, name=""):
	global options
	if name and name[0] == ".": return name
	for opt, arg in options:
		filename = get_filename(name)
		extension = get_extension(name)
		if opt == "-h":
			for docline in [
				"\nUSAGE [-tuleRnzxrqwapiI] <FILE/DIRECTORY> [<FILE/DIRECTORY>]\n",
				"-t : Title Case filename",
				"-u : UPPERCASE filename",
				"-l : lowercase filename",
				"-e : lowercase extension",
				"-E : UPPERCASE extension",
				"-n : remove all non-numerical characters",
				"--alpha : remove all non-letter ascii characters",
				"-z <NEW EXTENSION> : change extension",
				"-x <PATTERN TO DELETE> : delete all instances of pattern",
				"-r <PATTERN TO REPLACE | NEW PATTERN> : replace all instaces of pattern, separated by ' | '",
				"-q <NUMBER OF CHARACTERS TO REMOVE> : truncate filename from the left",
				"-w <NUMBER OF CHARACTERS TO REMOVE> : truncate filename from the right",
				"-a <STRING> : append string to filename",
				"-p <STRING> : prepend string to filename",
				"-i <PADDING> : leftwardly enumerate all files and apply padding to numbers (padding 3 -> 001)",
				"-I <PADDING> : rightwardly enumerate all files and apply padding to numbers (padding 3 -> 001)"
				"\n"
			]: print docline
		else: name = actions[opt](filename, extension, arg)
	return name

def counter():
	num = 0
	while True:
		yield num + 1
		num += 1

def rename(other = ""):
	global options, arguments, counter, actions
	other = arguments if not other else [other]
	for file_folder_path in other:
		if file_folder_path and file_folder_path[0] == ".": continue
		if os.path.isdir(file_folder_path):
			folder = os.listdir(file_folder_path)
			for filename in folder:
				path = file_folder_path + "/"
				if os.path.isdir(path + filename): rename(os.path.abspath(file_folder_path + "/" + filename))
				else:
					old_name = path + filename
					new_name = path + handleoptions(actions, filename)
					os.rename(old_name, new_name)
		else:
			path, filename = os.path.split(file_folder_path)
			path += "/"
			old_filename = path + filename
			new_filename = path + handleoptions(actions, filename)
			os.rename(old_filename, new_filename)

def main():
	global options, arguments, counter, actions
	options, arguments = getopt.getopt(sys.argv[1:], "tz:lx:er:Eq:nw:ua:p:Ii:h", ["alpha"])
	counter = counter()

	actions = {
		# titlecase filename
		"-t" : lambda filename, extension, arg: filename.title() + extension,

		# uppercase filename
		"-u" : lambda filename, extension, arg: filename.upper() + extension,

		# lowercase filename
		"-l" : lambda filename, extension, arg: filename.lower() + extension,

		# lowercase extension
		"-e" : lambda filename, extension, arg: filename + extension.lower(),

		# uppercase extension
		"-E" : lambda filename, extension, arg: filename + extension.upper(),

		# only allow numbers
		"-n" : lambda filename, extension, arg: "".join([x for x in filename if x.isdigit()]) + extension,

		# only allow basic ascii letters
		"--alpha" : lambda filename, extension, arg: "".join([x for x in filename if x in "abcdefghijklmnopqrstuvwxyz"]) + extension,

		# change extension
		"-z" : lambda filename, extension, arg: filename + arg if arg[0] == "." else filename + "." + arg,

		# delete all instances of pattern
		"-x" : lambda filename, extension, arg: filename.replace(arg, "") + extension,

		# replace string (delimited by " | ") in filename
		"-r" : lambda filename, extension, arg: filename.replace(arg.split(" | ")[0], arg.split(" | ")[1]) + extension,

		# truncate from left
		"-q" : lambda filename, extension, arg: filename[int(arg):] + extension,

		# truncate from right
		"-w" : lambda filename, extension, arg: filename[:int(arg)] + extension,

		# append to filename
		"-a" : lambda filename, extension, arg: filename + arg + extension,

		# prepend to filename
		"-p" : lambda filename, extension, arg: arg + filename + extension,

		# enumerate leftwardly
		"-i" : lambda filename, extension, arg: "{0} {1}{2}".format(pad(counter.next(), arg), filename, extension),

		# enumerate rightwardly
		"-I" : lambda filename, extension, arg: "{1}{2} {0}".format(pad(counter.next(), arg), filename, extension)

	}

	handleoptions(actions)
	rename()

if __name__ == '__main__':
	main()