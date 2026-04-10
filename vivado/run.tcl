set file_name [lindex $argv 0]
set top_module [lindex $argv 1]

read_verilog $file_name

synth_design -top $top_module

report_utilization -file results/util_$top_module.txt

# USE THIS INSTEAD
report_timing -max_paths 5 -file results/timing_$top_module.txt

exit
