

def load_config():
    file_path = "config.txt"
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                
                # Skip empty lines or lines starting with '#'
                if not line or line.startswith('#'):
                    continue

                # Split line into key and value
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()

                    # Store in dictionary
                    config[key] = value
                else:
                    print(f"Warning: Skipping invalid line (missing '='): {line}")
    except FileNotFoundError:
        print(f"Config file {file_path} not found.")
    except Exception as e:
        print(f"Error reading config file: {e}")

    return config

if __name__ == "__main__":  
    # Load and return the configuration
    config = load_config()
    print(config)
