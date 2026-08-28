"""Breaking apart strings is a surprisingly common task."""

t_str = "This is a\ntest sentence."
split_str = t_str.split()
print(split_str)

test_split = t_str.split("test")
beginning_split = t_str.split("This is a")
missing_split = t_str.split(", ")
print(test_split)
print(beginning_split)
print(missing_split)

movie_files = [
    "The Shawshank Redemption.mp4",
    "Inception.mkv",
    "The Dark Knight.avi",
    "Pulp Fiction.mov",
    "Fight Club.mp4",
]

for movie in movie_files:
    split_filename = movie.split()
    join_filename = "_".join(split_filename)
    print(join_filename)
