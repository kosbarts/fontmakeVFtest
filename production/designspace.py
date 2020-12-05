import sys

# Check and collect file inputs and outputs
if("--helper" in sys.argv):
	helperFile = sys.argv[sys.argv.index("--helper") + 1]
else:
	print("Please specify a helper file with the flag --helper 'path/to/helper'")
	sys.exit()

if("--output" in sys.argv):
	outputFile = sys.argv[sys.argv.index("--output") + 1]
else:
	print("Please specify an output file with the flag --output 'path/to/output'")
	sys.exit()

# Gather the ruleset from the helper
with open(helperFile, 'r') as hf:
	contents = hf.read()
	soup = BeautifulSoup(contents, 'lxml')
	helperRules = soup.rules # Find the <rules> and store for later

# Open the output file and replace the ruleset with the one from the helper file
with open(outputFile, 'r+') as of:
	contents = of.read()
	soup = BeautifulSoup(contents, 'lxml') # Run BS on the contents
	soup.rules.replaceWith(helperRules) # Find the <rules> and replace it with the helperFile's <rules>
# Replace the rules
	stringSoup = str(soup.designspace.prettify()) # Convert to string for writing ## Note: digging directly to soup.designspace because at some point bs appended html.body...
	header = "<?xml version='1.0' encoding='UTF-8'?>" # Standard xml header

# Overwrite file
	of.seek(0) # Move to the start of the file
	of.write(header + "\n") # Write the "<?xml..." header and a newline

	write = of.write(stringSoup) # Write
	of.truncate() # Cut the rest of the file if it exists...

print("Time for a beer! \U0001F37B")
