with open("wikipedia-sentences.csv") as fin, open("wiki.csv", "w") as fout:
	for line in fin:
		if "\t" not in line:
			fout.write(line.replace(' ', '\t', 1))
		else:
			fout.write(line)
#to solve the issue of spacing
