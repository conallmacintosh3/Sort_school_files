# Sort_school_files
Intended to sorts school files by class name and assignment name

The main script is sort_files.py 

In order for this script to actually work, there is currently a limitation:
  The naming structure of your file should be -> [CLASS] [#]-[Assignment Name]_[desc].[filetype]
      Example: ABC 101-Assignment 1_description here.docx

The first time you run it, the script will automatically create a new directory if it does not existing using the given base directory, name of the class, and the name of the assignment. Therefore, if the structure is not followed as above and is different everytime, then the script will keep writing new directories instead of putting it into its proper designation. 

**Before running there are certain things that need to be done:**
1. Put in your base directory under `base_directory` 
2. insert the current user name into the variables `base_directory` and `desktop`

Lastly, I have currently on a limited number of filetypes.. Feel free to add more under the variable `FILETYPES`. It shouldn't cause any issues as long as your follow the current structure. 


*NOTE:* As of this posting I'm still a new developer so please feel free to critique and improve what I arleady have. 
