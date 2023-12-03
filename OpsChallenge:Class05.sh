#!/bin/bash

# Define log files
log_files=("/var/log/syslog" "/var/log/wtmp")

# Define backup directory
backup_dir="/var/log/backups"

# Create backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Print original file sizes
echo "Original file sizes:"
for file in "${log_files[@]}"; do
    size=$(du -h "$file" | cut -f1)
    echo "$file: $size"
done

# Compress and backup log files
timestamp=$(date +"%Y%m%d%H%M%S")
for file in "${log_files[@]}"; do
    base_name=$(basename "$file")
    compressed_file="$backup_dir/$base_name-$timestamp.zip"
    gzip -c "$file" > "$compressed_file"
    echo "Compressed $file to $compressed_file"
    # Clear log file
    truncate -s 0 "$file"
done

# Print compressed file sizes
echo -e "\nCompressed file sizes:"
for file in "${log_files[@]}"; do
    base_name=$(basename "$file")
    compressed_file="$backup_dir/$base_name-$timestamp.zip"
    size=$(du -h "$compressed_file" | cut -f1)
    echo "$compressed_file: $size"
done

# Compare sizes
echo -e "\nSize comparison:"
for file in "${log_files[@]}"; do
    base_name=$(basename "$file")
    original_size=$(du -h "$file" | cut -f1)
    compressed_file="$backup_dir/$base_name-$timestamp.zip"
    compressed_size=$(du -h "$compressed_file" | cut -f1)
    echo "$file: $original_size vs $compressed_file: $compressed_size"
done
