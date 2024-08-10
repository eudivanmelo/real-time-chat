
class Formatter:
    """
    Formatter class for formatting data.
    """
    def format_bytes(bytes_num):
        """
        Formats bytes to a human-readable string.
        
        Args:
            bytes_num (int): The number of bytes.
        
        Returns:
            str: The formatted string.
        """
        suffixes = ['B', 'KB', 'MB', 'GB']
        index = 0
        
        while bytes_num >= 1024 and index < len(suffixes) - 1:
            bytes_num /= 1024.0
            index += 1
        
        return f"{bytes_num:.2f} {suffixes[index]}"
