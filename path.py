import psutil

# Print out disk partitions
print("Disk Partitions:")
for partition in psutil.disk_partitions():
    print(partition)

# Rest of the code remains unchanged

partitions = psutil.disk_partitions()
for partition in partitions:
    print(partition.mountpoint)
