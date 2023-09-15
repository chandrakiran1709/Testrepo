import sys

def cla_files(input_file_path, output_file_path):
    try:
        
        if not input_file_path or not output_file_path:
            raise ValueError("Enter valid number of files.")
        
   
        try:
            with open(input_file_path, 'r') as input_file:
                 data = input_file.read()
        except FileNotFoundError:
            raise FileNotFoundError("No such file or directory")
            processed_data = data.upper()  
        
      
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_data)
        
        print("cla_File processing completed")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)  


    if len(sys.argv) != 3:
        print("enter the command in proper format")
        sys.exit(1)

        
        
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
cla_files(input_file_path, output_file_path)