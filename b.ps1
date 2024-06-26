if ($args.Length -eq 1) {
    jumper.py b -c $args[0] | Set-Location
}
else {
    jumper.py b | Set-Location 
}