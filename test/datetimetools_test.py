from drewcopytools.datetimetools import get_aligned_utc_time
from pathlib import Path
from drewcopytools import filetools

# ------------------------------------------------------------------------------------------------------------------------
def test_can_get_aligned_utc_time():
  time = get_aligned_utc_time()

  assert time.hour == 0
  assert time.minute == 0
  assert time.second == 0


# ------------------------------------------------------------------------------------------------------------------------
def test_can_usePathInSequentialFilenameGenerator():
  """Shows that str or path can be used when generating sequential file names."""

  MY_FILE  = "MYFILE"
  EXT = ".txt"
  dir1 = Path("./")
  path1 = filetools.get_sequential_file_path(dir1, MY_FILE, EXT)

  dir2 = "./"
  path2 = filetools.get_sequential_file_path(dir2, MY_FILE, EXT)

  # The paths should be the same....
  assert path1 == path2