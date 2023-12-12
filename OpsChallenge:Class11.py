import psutil

# Get CPU times
cpu_times = psutil.cpu_times()

# Extract information
user_time = cpu_times.user
system_time = cpu_times.system
idle_time = cpu_times.idle
nice_time = cpu_times.nice
iowait_time = cpu_times.iowait
irq_time = cpu_times.irq
softirq_time = cpu_times.softirq
steal_time = cpu_times.steal
guest_time = cpu_times.guest

# Print results
print("Time spent by normal processes executing in user mode:", user_time)
print("Time spent by processes executing in kernel mode:", system_time)
print("Time when system was idle:", idle_time)
print("Time spent by priority processes executing in user mode:", nice_time)
print("Time spent waiting for I/O to complete:", iowait_time)
print("Time spent for servicing hardware interrupts:", irq_time)
print("Time spent for servicing software interrupts:", softirq_time)
print("Time spent by other operating systems running in a virtualized environment:", steal_time)
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", guest_time)
