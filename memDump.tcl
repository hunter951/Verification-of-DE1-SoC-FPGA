# memDump.tcl
# Author: Hunter Frederick
# Usage: \path_to_quartus_installation\quartus_stp -t \memDump.tcl
# Identifies connected DE1-SoC FPGA to computer then begins extracting data from RAMs on board during FPGA operation.

foreach hardware_name [get_hardware_names] {
	set hw_name $hardware_name
}

# Identifies chip on DE1-SoC.
foreach device_name [get_device_names -hardware_name $hw_name] {
	puts $device_name
	if { [string match "*5CSE*" $device_name] } {
		set dev_name $device_name
	}
}

foreach mem [get_editable_mem_instances -hardware_name $hw_name -device_name $dev_name] {
	lappend memories $mem
}

begin_memory_edit -hardware_name $hw_name -device_name $dev_name 

for { set i 0 } { $i < [llength $memories] } { incr i } {
	set fname RAM${i}.mif
	save_content_from_memory_to_file -instance_index $i -mem_file_path $fname -mem_file_type mif
}

end_memory_edit
