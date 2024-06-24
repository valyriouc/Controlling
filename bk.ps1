if ($args.Length -eq 1) {
    jumper.py b -c $args[0] | cd
}
else {
    jumper.py b | cd 
}