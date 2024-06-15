import os

output_dir = 'public'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Ensure to call the script using Python interpreter
os.system('python site.py')

print("Build completed!")
