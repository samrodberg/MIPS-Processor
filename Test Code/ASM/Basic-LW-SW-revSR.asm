#Author: John Rieffel
#NOTE: if your instruction word does not support immediates as large as 7,
# you will need to REWRITE this code in order to work with your processor
#
# results: values 0..7 should be in memory locations 0..7
# 	   values 7..0 should be in registers 0..7 (switched)

addi $1 $0 1
addi $2 $0 2
add  $3 $2 $1
add  $4 $2 $2
add $5 $3 $2
add  $6 $3 $3
add $7 $3 $4
sw   $1 0($1)
sw   $2 0($2)
sw   $3 0($3)
sw   $4 0($4)
sw   $5 0($5)
sw   $6 0($6)
sw   $7 0($7)
addi $0 $1 0
lw   $1 0($7)
lw   $7 0($0)
addi $0 $2 0
lw   $2 0($6)
lw   $6 0($0)
addi $0 $3 0
lw   $3 0($5)
lw   $5 0($0)
