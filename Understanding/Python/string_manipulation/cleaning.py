"""Strings can be messy; often needing to be cleaned."""

# strip
dirty = "  another example\tstring.   \n"
stripped = dirty.strip()
print(stripped)

more_stripped = dirty.strip(" \n.!?ag")
print(more_stripped)

# replace
no_space = dirty.replace(" ", "")
print(no_space)

rewrite = dirty.replace("example\t", "perfect example ")
print(rewrite)

movie_files = [
    "The Shawshank Redemption.mp4",
    "Inception.mkv",
    "The Dark Knight.avi",
    "Pulp Fiction.mov",
    "Fight Club.mp4",
]

for movie in movie_files:
    print(movie.replace(" ", "_"))
